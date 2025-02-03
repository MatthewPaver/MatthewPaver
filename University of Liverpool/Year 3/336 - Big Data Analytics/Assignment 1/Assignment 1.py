# Filename: PART-1.py
# Description: PySpark script for analysing GPS trajectory data from the Geolife project.
# Requirements: Ensure the file 'dataset.txt' is in the same directory as this script.
#               This file should contain the GPS data with columns as specified in the assignment.
# 
# Instructions for Running:
# Run this script in your desired IDE and select the run button to execute the code.
#
# Environment: This code is compatiable with PySpark 3.5.3 and Python 3.10.12

# Import necessary PySpark and Python libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, udf, weekofyear, lag, max as spark_max, min as spark_min, sum as spark_sum
from pyspark.sql.window import Window
import math
import os

# Start a Spark session
spark = SparkSession.builder \
    .appName("Big Data Assignment 1") \
    .getOrCreate()

# Get the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path
file_path = os.path.join(current_dir, "dataset.txt")

# Read the CSV file
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Task 1: Convert timestamps to local time zone based on longitude
from pyspark.sql.functions import col, udf
from pyspark.sql.types import DoubleType, IntegerType

# Define the function to calculate timezone offset based on longitude
def calculate_offset(longitude):
    # Calculate the timezone offset based on the longitude (15 degrees per hour)
    return int(longitude // 15)

# Define the function to adjust timestamp using the calculated offset
def adjust_timestamp(longitude, timestamp):
    offset = calculate_offset(longitude)
    return timestamp + offset / 24  # Adjust timestamp by offset in days

# Register User Defined Functions (UDFs)
calculate_offset_udf = udf(calculate_offset, IntegerType())
adjust_timestamp_udf = udf(adjust_timestamp, DoubleType())

# Apply the UDFs to add offset and adjusted timestamp columns
df = df.withColumn("Offset_Hours", calculate_offset_udf(col("Longitude"))) \
       .withColumn("Adjusted_Timestamp", adjust_timestamp_udf(col("Longitude"), col("Timestamp")))

# Show a limited number of rows with relevant columns to verify adjustments
df.select("UserID", "Latitude", "Longitude", "Timestamp", "Offset_Hours", "Adjusted_Timestamp").show(10)  # Show only 10 rows

# Task 2: Filter records within Beijing's borders
df_beijing = df.filter(
    (col("Latitude") >= 39.5) & (col("Latitude") <= 40.5) &
    (col("Longitude") >= 115.5) & (col("Longitude") <= 117.5)
)

# Output count of records in Beijing
print(f"Number of records in Beijing: {df_beijing.count()}")

# Task 3: Calculate the number of days each user recorded more than 10 data points
df_grouped_by_user_day = df.groupBy("UserID", "Date").count().filter(col("count") > 10)
df_days_per_user = df_grouped_by_user_day.groupBy("UserID").count()

# Output top 6 users ranked by the number of days
df_days_per_user.orderBy(col("count").desc(), col("UserID")).show(6)

# Task 4: Calculate the number of weeks each user recorded more than 100 data points
df_with_week = df.withColumn("Week", weekofyear(col("Date")))

df_grouped_by_user_week = df_with_week.groupBy("UserID", "Week").count().filter(col("count") > 100)
df_weeks_per_user = df_grouped_by_user_week.groupBy("UserID").count()

# Output user ID along with the count of weeks
df_weeks_per_user.orderBy(col("count").desc(), col("UserID")).show(6)

# Task 5: Find the northernmost point (greatest Latitude) for each user
df_northernmost = df.groupBy("UserID").agg(
    spark_max("Latitude").alias("MaxLatitude"),
    spark_max("Date").alias("Date")
)

# Output top 6 users based on MaxLatitude
df_northernmost.orderBy(col("MaxLatitude").desc(), col("UserID")).show(6)

# Check if these top users have any records within Beijing
df_northernmost_beijing = df_northernmost.join(
    df_beijing.select("UserID").distinct(),
    "UserID", "left_outer"
).withColumn("InBeijing", col("UserID").isNotNull())

# Output whether the top users have been to Beijing
df_northernmost_beijing.select("UserID", "InBeijing").show(6)

# Task 6: Calculate daily altitude span for each user (Max Altitude - Min Altitude per day)
df_altitude_span = df.groupBy("UserID", "Date").agg(
    (spark_max("Altitude") - spark_min("Altitude")).alias("AltitudeSpan")
)

# Find the maximum altitude span for each user across all days
df_max_altitude_span = df_altitude_span.groupBy("UserID").agg(
    spark_max("AltitudeSpan").alias("MaxAltitudeSpan")
)

# Output top 6 users based on max altitude span
df_max_altitude_span.orderBy(col("MaxAltitudeSpan").desc(), col("UserID")).show(6)

# Task 7: Calculate total distance travelled per day for each user
def calculate_distance(lat1, lon1, lat2, lon2):
    if lat1 is None or lon1 is None or lat2 is None or lon2 is None:
        return 0.0  # Return 0 distance if any of the coordinates are None
    # Haversine formula to calculate the distance between two points on Earth
    R = 6371  # Earth radius in kilometers
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = math.sin(d_lat / 2) ** 2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(d_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Register the UDF for distance calculation
distance_udf = udf(calculate_distance)

# Create a window to calculate the distance between consecutive points
window_spec = Window.partitionBy("UserID", "Date").orderBy("Timestamp")

# Calculate distance between consecutive points
df_with_distance = df.withColumn(
    "Distance",
    distance_udf(
        lag("Latitude", 1).over(window_spec), lag("Longitude", 1).over(window_spec),
        col("Latitude"), col("Longitude")
    )
)

# Sum up daily distance travelled by each user
df_daily_distance = df_with_distance.groupBy("UserID", "Date").agg(
    spark_sum("Distance").alias("TotalDistance")
)

# Find the day with the maximum distance for each user
df_max_daily_distance = df_daily_distance.groupBy("UserID").agg(
    spark_max("TotalDistance").alias("MaxDistance")
)

# Output the top 6 users based on maximum distance travelled in a day
df_max_daily_distance.orderBy(col("MaxDistance").desc(), col("UserID")).show(6)

# Calculate the total distance travelled by all users
total_distance = df_daily_distance.agg(spark_sum("TotalDistance")).collect()[0][0]
print(f"Total distance travelled by all users: {total_distance:.2f} km")

# Stop the Spark session
spark.stop()