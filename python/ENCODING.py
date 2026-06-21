import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('data/placement_data.csv')

# Create encoded columns
df['Internship_Enc'] = df['Internship'].map({'Yes': 1, 'No': 0})
df['Placed_Enc'] = df['Placed'].map({'Yes': 1, 'No': 0})

# Placement Rate
print("Placement Rate:\n")
print(df['Placed'].value_counts(normalize=True) * 100)

# CGPA vs Placement
plt.figure(figsize=(6,4))
sns.boxplot(x='Placed', y='CGPA', data=df)
plt.title("CGPA vs Placement")
plt.show()

# Internship vs Placement
plt.figure(figsize=(6,4))
sns.countplot(x='Internship', hue='Placed', data=df)
plt.title("Internship vs Placement")
plt.show()

# Salary Distribution
plt.figure(figsize=(6,4))
sns.histplot(df['Salary_LPA'], bins=10, kde=True)
plt.title("Salary Distribution")
plt.show()

# Correlation Heatmap
corr_cols = [
    'CGPA',
    '10th_Percentage',
    '12th_Percentage',
    'Mock_Score',
    'Salary_LPA',
    'Internship_Enc',
    'Placed_Enc'
]

plt.figure(figsize=(8,5))
sns.heatmap(df[corr_cols].corr(), annot=True, cmap='coolwarm')

plt.title("Correlation Heatmap")
plt.show()

print("EDA Completed Successfully")