-- Placement rate with/without internship
SELECT
    Internship,
    COUNT(*) AS total,
    SUM(CASE WHEN Placed='Yes' THEN 1 ELSE 0 END) AS placed,
    ROUND(AVG(CASE WHEN Placed='Yes' THEN 1.0 ELSE 0 END)*100,1) AS placement_pct,
    ROUND(AVG(CASE WHEN Placed='Yes' THEN Salary_LPA END),2) AS avg_salary_lpa
FROM placement_data
GROUP BY Internship;