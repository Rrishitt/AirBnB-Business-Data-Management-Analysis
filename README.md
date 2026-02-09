# 🏙️ Airbnb NYC 2019 — Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project performs a **comprehensive exploratory data analysis (EDA)** on the Airbnb NYC 2019 dataset to uncover insights related to pricing, availability, room types, and demand across different boroughs of New York City.

The goal is to demonstrate **real-world data analysis skills** using Python — focusing on data cleaning, feature engineering, visualization, and insight generation — in a way that aligns with industry expectations.

---

## 🎯 Objectives
- Understand pricing behavior across NYC boroughs
- Analyze the impact of room type and availability on pricing
- Examine relationships between reviews, demand, and price
- Practice structured, reproducible EDA using Python

---

## 🗂️ Dataset Information
- **Dataset:** Airbnb NYC 2019
- **Rows:** 48,895
- **Columns:** 16
- **Key Features:**
  - `price`
  - `room_type`
  - `neighbourhood_group`
  - `availability_365`
  - `number_of_reviews`
  - `reviews_per_month`
  - `minimum_nights`

---

## 🛠️ Tech Stack
- **Python 3**
- **NumPy** – numerical computation  
- **Pandas** – data manipulation and cleaning  
- **Matplotlib** – data visualization  
- **Seaborn** – statistical visualization  

The project is implemented as a **standalone Python script** (not a notebook), simulating a production-style workflow.

---

## 🔍 Analysis Workflow

### 1️⃣ Data Cleaning
- Converted date columns to `datetime`
- Handled missing values using logical assumptions
- Removed invalid listings with zero price
- Preserved real-world outliers for transparency

### 2️⃣ Feature Engineering
- Created price categories:
  - Budget
  - Mid-range
  - Premium
  - Luxury
  - Ultra-Luxury

### 3️⃣ Exploratory Analysis
- Price distribution analysis
- Comparison of prices across room types
- Borough-level listing density
- Availability vs price behavior
- Correlation analysis between numerical variables

### 4️⃣ Data Visualization
All visualizations are rendered **live during script execution**:
- Histogram (price distribution)
- Box plot (price vs room type)
- Count plot (listings per borough)
- Scatter plot (availability vs price)
- Bar chart (average price by borough)
- Correlation heatmap

---

## 📊 Key Insights
- Manhattan listings have the highest average prices.
- Entire home/apartment listings dominate higher price ranges.
- Review count shows weak correlation with price.
- Brooklyn offers better affordability compared to Manhattan.
- Availability does not strongly influence pricing.

---

## ▶️ How to Run the Project

### 1. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn
