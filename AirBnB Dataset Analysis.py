# =========================================================
# Airbnb NYC 2019 - FINAL EDA SCRIPT (VISUAL OUTPUT ONLY)
# Author: Rishit
# =========================================================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------
# CONFIG
# -------------------------
DATA_PATH = r"C:\Users\Rishit\OneDrive\Desktop\Airbnb NYC 2019.csv"

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)


# -------------------------
# LOAD DATA
# -------------------------
def load_data(path):
    df = pd.read_csv(path)
    print("\nDataset Loaded")
    print("Shape:", df.shape)
    return df


# -------------------------
# DATA CLEANING
# -------------------------
def clean_data(df):
    print("\n--- MISSING VALUES (%) BEFORE CLEANING ---")
    print((df.isnull().mean() * 100).sort_values(ascending=False))

    # Convert to datetime
    df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

    # Logical imputations
    df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
    df['host_name'] = df['host_name'].fillna("Unknown")
    df['name'] = df['name'].fillna("Unknown")

    # Remove invalid prices
    df = df[df['price'] > 0]

    print("\nData cleaned.")
    return df


# -------------------------
# BASIC EXPLORATION
# -------------------------
def exploration(df):
    print("\n--- HEAD ---")
    print(df.head())

    print("\n--- INFO ---")
    df.info()

    print("\n--- NUMERICAL SUMMARY (CLEANED) ---")
    print(df.describe())


# -------------------------
# FEATURE ENGINEERING
# -------------------------
def feature_engineering(df):
    df['price_category'] = pd.cut(
        df['price'],
        bins=[0, 100, 200, 300, 500, np.inf],
        labels=['Budget', 'Mid-range', 'Premium', 'Luxury', 'Ultra-Luxury']
    )
    return df


# -------------------------
# VISUALIZATIONS (DISPLAY ONLY)
# -------------------------
def visualizations(df):
    # Cap extreme values for readability (visual only)
    price_cap = df['price'].quantile(0.99)
    viz_df = df[df['price'] <= price_cap]

    # 1️⃣ Price Distribution (Histogram)
    sns.histplot(viz_df['price'], bins=50, kde=True)
    plt.title("Price Distribution (≤ 99th Percentile)")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.show()

    # 2️⃣ Price by Room Type (Box Plot)
    sns.boxplot(x='room_type', y='price', data=viz_df)
    plt.title("Price by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Price")
    plt.show()

    # 3️⃣ Listings by Neighbourhood Group (Count Plot)
    sns.countplot(x='neighbourhood_group', data=df)
    plt.title("Number of Listings by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Listings Count")
    plt.show()

    # 4️⃣ Availability vs Price (Scatter Plot)
    sns.scatterplot(
        x='availability_365',
        y='price',
        data=viz_df,
        alpha=0.4
    )
    plt.title("Availability vs Price")
    plt.xlabel("Availability (days/year)")
    plt.ylabel("Price")
    plt.show()

    # 5️⃣ Average Price per Borough (Bar Plot)
    df.groupby('neighbourhood_group')['price'].mean().plot(kind='bar')
    plt.title("Average Price by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Average Price")
    plt.show()

    # 6️⃣ Correlation Heatmap
    corr = df[['price', 'minimum_nights', 'number_of_reviews',
               'reviews_per_month', 'availability_365']].corr()

    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()


# -------------------------
# FINAL INSIGHTS
# -------------------------
def conclusions():
    print("""
--- FINAL INSIGHTS ---
1. Manhattan has the highest average listing prices.
2. Entire home/apt listings dominate the premium price range.
3. Number of reviews has weak correlation with price.
4. Brooklyn offers better affordability compared to Manhattan.
5. Availability does not strongly influence pricing.
""")


# -------------------------
# MAIN EXECUTION
# -------------------------
def main():
    df = load_data(DATA_PATH)
    df = clean_data(df)
    exploration(df)
    df = feature_engineering(df)
    visualizations(df)
    conclusions()

    print("\nEDA COMPLETE — ALL VISUALS DISPLAYED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
