-- Placement rate by CGPA band
SELECT
    CASE
        WHEN CGPA < 6.5  THEN 'Below 6.5'
        WHEN CGPA < 7.5  THEN '6.5 – 7.5'
        WHEN CGPA < 8.5  THEN '7.5 – 8.5'
        ELSE '8.5 and above'
    END AS cgpa_band,
    COUNT(*) AS total,
    SUM(CASE WHEN Placed='Yes' THEN 1 ELSE 0 END) AS placed,
    ROUND(AVG(CASE WHEN Placed='Yes' THEN 1.0 ELSE 0 END)*100,1) AS rate_pct
FROM placement_data
GROUP BY cgpa_band
ORDER BY MIN(CGPA);