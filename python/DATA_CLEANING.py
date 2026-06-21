import pandas as pd
import numpy as np

# ✅ LOAD DATA (THIS IS MISSING)
df = pd.read_csv('data/placement_data.csv')
# ── Check missing values ──────────────────────────
print("Missing values:\n", df.isnull().sum())

# Fill numeric columns with median (robust to outliers)
num_cols = ['CGPA', '10th_Percentage', '12th_Percentage',
            'Mock_Score', 'Salary_LPA']

for col in num_cols:
    df[col].fillna(df[col].median(), inplace=True)

# Fill categorical columns with mode
cat_cols = ['Skills', 'Internship', 'Placed']
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Strip whitespace from string columns
df['Skills'] = df['Skills'].str.strip()
df['Internship'] = df['Internship'].str.strip()
df['Placed'] = df['Placed'].str.strip()

# Validate CGPA range
df = df[(df['CGPA'] >= 5.0) & (df['CGPA'] <= 10.0)]
df = df[(df['Mock_Score'] >= 0) & (df['Mock_Score'] <= 100)]

print("Cleaned dataset shape:", df.shape)
df.to_csv('data/cleaned_placement_data.csv', index=False)
print("Cleaned file saved successfully!")