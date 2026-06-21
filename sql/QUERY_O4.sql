-- Placement rate and avg salary per skill
SELECT
    Skills,
    COUNT(*) AS total_students,
    SUM(CASE WHEN Placed='Yes' THEN 1 ELSE 0 END) AS placed_count,
    ROUND(AVG(CASE WHEN Placed='Yes'
             THEN 1.0 ELSE 0 END)*100,1) AS placement_rate_pct,
    ROUND(AVG(CASE WHEN Placed='Yes' THEN Salary_LPA END),2) AS avg_salary_lpa
FROM placement_data
GROUP BY Skills
ORDER BY placement_rate_pct DESC;