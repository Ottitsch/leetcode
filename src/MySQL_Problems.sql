-- My MySQL Solutions To The SQL 50 From Leetcode
-- Recyclable and Low Fat Products
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = "Y"

-- Find Customer Referee
SELECT name
FROM Customer
WHERE referee_id is NULL or referee_id != 2

-- Big Countries
SELECT name, population, area
FROM World
WHERE area >= 3000000 or population >= 25000000

-- Article Views I
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id

-- Invalid Tweets
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15

-- Replace Employee ID With The Unique Identifier
SELECT eu.unique_id AS unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu USING(id)