#Data Preparation
import pandas as pd
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("C:/Users/Rashika Ranjan/OneDrive/Desktop/DL-PROJECT/videos.csv")
print("Initial Data:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)
df.drop_duplicates(inplace=True)
df.to_csv('cleaded_video.csv', index=False)
print("\nCleande Data:")
print(df.head())