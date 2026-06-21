-- Full salary statistics for placed students
SELECT
    ROUND(MIN(Salary_LPA),2)    AS min_salary,
    ROUND(MAX(Salary_LPA),2)    AS max_salary,
    ROUND(AVG(Salary_LPA),2)    AS avg_salary,
    ROUND(STDDEV(Salary_LPA),2) AS std_dev
FROM placement_data
WHERE Placed = 'Yes';