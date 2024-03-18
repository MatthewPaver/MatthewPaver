-- Question 1:

-- Create Customers table
CREATE TABLE Customers (
    birth_day DATE,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    c_id INT PRIMARY KEY
);

-- Create Employees table
CREATE TABLE Employees (
    birth_day DATE,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    e_id INT PRIMARY KEY
);

-- Create BusType table
CREATE TABLE BusType (
    capacity INT,
    type VARCHAR(20) PRIMARY KEY
);

-- Create BusTrip table
CREATE TABLE BusTrip (
    start_time DATETIME,
    route_no INT,
    type VARCHAR(20),
    e_id INT,
    b_id INT PRIMARY KEY,
    FOREIGN KEY (type) REFERENCES BusType(type),
    FOREIGN KEY (e_id) REFERENCES Employees(e_id)
);

-- Create TicketCosts table
CREATE TABLE TicketCosts (
    cost INT,
    duration VARCHAR(20) PRIMARY KEY
);

-- Create CustomerTrip table
CREATE TABLE CustomerTrip (
    from_stop_no INT,
    to_stop_no INT,
    b_id INT,
    c_id INT,
    PRIMARY KEY (from_stop_no, to_stop_no),
    FOREIGN KEY (b_id) REFERENCES BusTrip(b_id),
    FOREIGN KEY (c_id) REFERENCES Customers(c_id)
);


-- Question 2

CREATE VIEW LouiseTrips AS
SELECT COUNT(*) AS number_of_trips
FROM Employees e
JOIN BusTrip b ON e.e_id = b.e_id
WHERE e.first_name = 'Louise' AND e.last_name = 'Davies'
AND MONTH(b.start_time) = 9 AND YEAR(b.start_time) = 2023;

-- Sample query to check the result
SELECT * FROM LouiseTrips;

-- Question 3 (Come back to)

CREATE VIEW PeopleOnRoute AS
-- Fetch customers who have been on route 102
(SELECT c.birth_day, c.first_name, c.last_name
FROM Customers c
JOIN CustomerTrip ct ON c.c_id = ct.c_id
JOIN BusTrip b ON ct.b_id = b.b_id
WHERE b.route_no = 102)

UNION

-- Fetch employees who have driven on route 102
(SELECT e.birth_day, e.first_name, e.last_name
FROM Employees e
JOIN BusTrip b ON e.e_id = b.e_id
WHERE b.route_no = 102);


 SELECT * FROM PeopleOnRoute ORDER BY last_name, first_name;



-- Question 4

CREATE VIEW UpcomingBirthdays AS
-- Birthdays on or after 8th November in the current year
(SELECT birth_day, first_name, last_name, 1 AS order_col 
 FROM Employees 
 WHERE MONTH(birth_day) > 11 OR (MONTH(birth_day) = 11 AND DAYOFMONTH(birth_day) >= 8)
)
UNION
-- Birthdays before 8th November (i.e., they will be next year)
(SELECT birth_day, first_name, last_name, 2 AS order_col 
 FROM Employees 
 WHERE MONTH(birth_day) < 11 OR (MONTH(birth_day) = 11 AND DAYOFMONTH(birth_day) < 8)
)
ORDER BY order_col, MONTH(birth_day), DAYOFMONTH(birth_day);

SELECT * FROM UpcomingBirthdays;

-- Question 5 (Come back to)
CREATE VIEW OverfullBuses AS
SELECT ct1.b_id
FROM CustomerTrip ct1
JOIN CustomerTrip ct2 ON ct1.b_id = ct2.b_id AND ct2.from_stop_no <= ct1.from_stop_no AND ct2.to_stop_no > ct1.from_stop_no
JOIN BusTrip bt ON ct1.b_id = bt.b_id
JOIN BusType btype ON bt.type = btype.type
GROUP BY ct1.b_id, ct1.from_stop_no, btype.capacity
HAVING COUNT(ct2.c_id) > btype.capacity;

SELECT * FROM OverfullBuses ORDER BY b_id;

-- Question 6 (Come back to)
CREATE VIEW PricePerDay AS
WITH DailyTrips AS (
    SELECT c_id, DATE(start_time) AS trip_date, COUNT(*) AS trip_count
    FROM CustomerTrip
    JOIN BusTrip ON CustomerTrip.b_id = BusTrip.b_id
    GROUP BY c_id, DATE(start_time)
)

SELECT 
    DailyTrips.c_id, 
    DailyTrips.trip_date as date,
    CASE 
        WHEN DailyTrips.trip_count * (SELECT cost FROM TicketCosts WHERE duration = 'single') <= (SELECT cost FROM TicketCosts WHERE duration = 'day') THEN DailyTrips.trip_count * (SELECT cost FROM TicketCosts WHERE duration = 'single')
        ELSE (SELECT cost FROM TicketCosts WHERE duration = 'day')
    END AS cost
FROM DailyTrips;

SELECT * FROM PricePerDay ORDER BY c_id,date;

-- Question 7 (Come back to)
CREATE VIEW PricePerWeek AS
WITH WeeklyTrips AS (
    SELECT 
        c_id, 
        WEEK(start_time, 7) AS trip_week, 
        YEAR(start_time) AS trip_year,
        COUNT(DISTINCT DATE(start_time)) AS days_traveled,
        COUNT(*) AS trip_count
    FROM CustomerTrip
    JOIN BusTrip ON CustomerTrip.b_id = BusTrip.b_id
    GROUP BY c_id, WEEK(start_time, 7), YEAR(start_time)
)

SELECT 
    WeeklyTrips.c_id, 
    WeeklyTrips.trip_week as week,
    WeeklyTrips.trip_year as year,
    CASE 
        WHEN (days_traveled * (SELECT cost FROM TicketCosts WHERE duration = 'day') + (trip_count - days_traveled) * (SELECT cost FROM TicketCosts WHERE duration = 'single')) <= (SELECT cost FROM TicketCosts WHERE duration = 'week') THEN days_traveled * (SELECT cost FROM TicketCosts WHERE duration = 'day') + (trip_count - days_traveled) * (SELECT cost FROM TicketCosts WHERE duration = 'single')
        ELSE (SELECT cost FROM TicketCosts WHERE duration = 'week')
    END AS cost
FROM WeeklyTrips;

SELECT * FROM PricePerWeek ORDER BY c_id, week, year;


