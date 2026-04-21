# PROGRAM: Outlier Detection using Box Plot (Alternative Method)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
df = pd.read_csv('4laptops.csv', engine='python', on_bad_lines='skip')

print("Dataset Info:")
print(df.info())


# -------------------------------
# Step 2: Convert RAM column if exists
# -------------------------------
if 'RAM' in df.columns:
    try:
        df['RAM'] = df['RAM'].str.replace('GB', '').astype(float)
    except:
        pass


# -------------------------------
# Step 3: Plot each column separately (Matplotlib)
# -------------------------------
print("\nMatplotlib Box Plots (Column-wise):")

for col in df.select_dtypes(include=['int64', 'float64']).columns:
    plt.figure()
    plt.boxplot(df[col])
    plt.title(f"Box Plot of {col} (Matplotlib)")
    plt.xlabel(col)
    plt.show()


# -------------------------------
# Step 4: Plot using Seaborn (Single column example)
# -------------------------------
print("\nSeaborn Box Plot:")

# Choose one column (example: RAM or first numeric column)
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

if len(num_cols) > 0:
    plt.figure()
    sns.boxplot(y=df[num_cols[0]])
    plt.title(f"Box Plot of {num_cols[0]} (Seaborn)")
    plt.show()
