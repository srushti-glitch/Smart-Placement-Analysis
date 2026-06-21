-- Q6: Top 10 salary earners
SELECT Student_ID, CGPA, Skills, Salary_LPA
FROM placement_data
WHERE Placed = 'Yes'
ORDER BY Salary_LPA DESC
LIMIT 10;

-- Q7: Students with high CGPA but not placed (risk group)
SELECT Student_ID, CGPA, Skills, Internship, Mock_Score
FROM placement_data
WHERE CGPA >= 8.0 AND Placed = 'No'
ORDER BY CGPA DESC;

-- Q8: Avg mock score by placement
SELECT Placed,
       ROUND(AVG(Mock_Score),1) AS avg_mock,
       ROUND(AVG(CGPA),2)       AS avg_cgpa
FROM placement_data
GROUP BY Placed;

-- Q9: Internship + CGPA combo impact on salary
SELECT Internship,
    CASE WHEN CGPA >= 8 THEN 'High CGPA'
         ELSE 'Lower CGPA' END AS cgpa_group,
    ROUND(AVG(Salary_LPA),2) AS avg_salary
FROM placement_data
WHERE Placed = 'Yes'
GROUP BY Internship, cgpa_group
ORDER BY avg_salary DESC;