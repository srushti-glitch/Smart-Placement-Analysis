import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('data/placement_data.csv')

# Quick overview
print(df.head())
print(df.info())
print(df.describe())
print("Shape:", df.shape)