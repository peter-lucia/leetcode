# Write your MySQL query statement below
SELECT IFNULL(
    (SELECT Max(Employee.Salary) FROM Employee
    WHERE Employee.Salary NOT IN (SELECT Max(Employee.Salary) FROM Employee))
    , NULL) AS SecondHighestSalary;