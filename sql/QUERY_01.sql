-- Overall placement rate as percentage
SELECT
    COUNT(*) AS total_students,
    SUM(CASE WHEN Placed = 'Yes'
             THEN 1 ELSE 0 END) AS placed_count,
    ROUND(
        SUM(CASE WHEN Placed = 'Yes'
                 THEN 1.0 ELSE 0 END)
        / COUNT(*) * 100, 2
    ) AS placement_rate_pct
FROM placement_data;