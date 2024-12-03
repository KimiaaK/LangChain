-- Create a table example
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    base_salary DECIMAL(10, 2)
);

-- Insert data
INSERT INTO employees (id, name, base_salary)
VALUES (1, 'Alice', 60000.00);

-- Query data
SELECT DISTINCT base_salary AS "Second Highest Salary"
FROM employees
ORDER BY 
    base_salary DESC
    LIMIT 1
    OFFSET 1