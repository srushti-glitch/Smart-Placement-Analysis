import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/cleaned_placement_data.csv")

# Create encoded columns
df['Internship_Enc'] = df['Internship'].map({'Yes': 1, 'No': 0})
df['Placed_Enc'] = df['Placed'].map({'Yes': 1, 'No': 0})

# 1. Placement Rate
placement_rate = df['Placed'].value_counts(normalize=True) * 100
print("Placement Rate:\n", placement_rate)

# 2. CGPA vs Placement
plt.figure(figsize=(8,5))
sns.boxplot(x='Placed', y='CGPA', data=df)
plt.title('CGPA vs Placement Status')
plt.show()

# 3. Internship Impact
intern_place = df.groupby(['Internship', 'Placed']).size().unstack()
intern_place.plot(kind='bar', stacked=True, figsize=(7,4))
plt.title('Internship vs Placement')
plt.show()

# 4. Skills Distribution
plt.figure(figsize=(8,5))
skill_counts = df['Skills'].value_counts()
skill_counts.plot(kind='barh')
plt.title('Skill Distribution')
plt.show()

# 5. Correlation Heatmap
corr_cols = [
    'CGPA',
    '10th_Percentage',
    '12th_Percentage',
    'Mock_Score',
    'Internship_Enc',
    'Placed_Enc',
    'Salary_LPA'
]

plt.figure(figsize=(8,6))
sns.heatmap(
    df[corr_cols].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)
plt.title('Correlation Heatmap')
plt.show()

# 6. Salary Distribution
placed = df[df['Placed'] == 'Yes']

plt.figure(figsize=(8,5))
sns.histplot(
    placed['Salary_LPA'],
    bins=15,
    kde=True
)
plt.title('Salary Distribution (Placed Students)')
plt.show()

# 7. Mock Score vs Placement
plt.figure(figsize=(8,5))
sns.violinplot(
    x='Placed',
    y='Mock_Score',
    data=df
)
plt.title('Mock Score Distribution by Placement')
plt.show()