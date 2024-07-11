
# PySpark and Kafka Integration Example

## Overview
This repository provides an example of integrating PySpark with Apache Kafka for real-time data streaming and processing. The aim is to demonstrate how PySpark can be used to consume and process streaming data from Kafka topics, as well as perform basic DataFrame operations.

## Prerequisites

1. **Install Java Development Kit (JDK)**
    - Spark runs on Java 8, 11, or 17. Ensure you have one of these versions installed on your system.

2. **Apache Spark**
    - Download Apache Spark from the official [Spark download page](https://spark.apache.org/downloads.html).
    - Version: 3.5.1
    - Pre-Built for Apache Hadoop 3.3 and later
    - Add Spark and Hadoop to your environment variables:
        - [Hadoop link](https://github.com/steveloughran/winutils/tree/master)
        - Set paths:
            - `C:\Users\MattPaver\AppData\Local\hadoop`
            - `C:\Users\MattPaver\AppData\Local\spark`
        - Add these paths to your System Environment Variables.

3. **Install Python**
    - Ensure Python is installed on your system. Then, install PySpark using pip:
    ```bash
    pip install pyspark
    ```

4. **Install Kafka**
    - Download Apache Kafka from the official [Kafka download page](https://kafka.apache.org/downloads).
    - Add Kafka to your environment variables:
        - `C:\Users\MattPaver\AppData\Local\kafka`

## How It Works

### Step 1: Start Zookeeper
Navigate to your Kafka installation directory and run the following command to start Zookeeper:
```bash
zookeeper-server-start.bat ..\..\config\zookeeper.properties
```

### Step 2: Start Kafka Server
In another terminal, navigate to your Kafka installation directory and run the following command to start the Kafka server:
```bash
kafka-server-start.bat ..\..\config\server.properties
```

### Step 3: Create Kafka Topic
Create a Kafka topic named `test-topic` using the following command:
```bash
kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

### Step 4: Execute PySpark Script
Run the PySpark script to process streaming data from Kafka:
```bash
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 "C:\Users\MattPaver\OneDrive - The University of Liverpool\Year 3\Project\PySpark.py"
```

## PySpark Scripts

### Example 1: Basic DataFrame Creation and Display
This script demonstrates creating a simple DataFrame and displaying its contents:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example").getOrCreate()
data = [("James", "Smith"), ("Anna", "Rose"), ("Robert", "Williams")]
columns = ["FirstName", "LastName"]
df = spark.createDataFrame(data, columns)
df.show()
```

**Output:**
```
+---------+--------+
|FirstName|LastName|
+---------+--------+
|    James|   Smith|
|     Anna|    Rose|
|   Robert|Williams|
+---------+--------+
```

### Example 2: Real-Time Data Processing with Kafka
This script demonstrates how to read streaming data from Kafka and process it using PySpark:
```python
import os
os.environ['SPARK_HOME'] = 'C:/Users/MattPaver/AppData/Local/Spark'

from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder     .appName("RealTimeExample")     .getOrCreate()

# Read from Kafka
df = spark.readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "test-topic")     .load()

# Select key and value from Kafka message
df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

# Write to console
query = df.writeStream     .outputMode("append")     .format("console")     .start()

query.awaitTermination()
```

## Explanation

- **Environment Setup:** The script sets the Spark home environment variable.
- **Spark Session:** A Spark session is created with the application name "RealTimeExample".
- **Kafka Source:** The script reads streaming data from the Kafka topic `test-topic`.
- **Data Processing:** It selects the key and value from the Kafka message, casting them to strings.
- **Output:** The processed data is written to the console in append mode.

## Conclusion
This example demonstrates how to set up and run a PySpark application that processes real-time data from Kafka. By following the steps above, you can integrate PySpark with Kafka and process streaming data efficiently. Additionally, you have learned how to create and display a simple DataFrame using PySpark.
