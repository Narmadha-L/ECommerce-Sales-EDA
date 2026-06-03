# 🛒 E-Commerce Sales EDA

## 📌 Project Overview
Exploratory Data Analysis on a real UK-based e-commerce dataset 
containing 500,000+ transactions from December 2010 to December 2011.

## 🎯 Objective
Analyze sales trends, top products, country-wise revenue, 
and order value distribution to derive actionable business insights.

## 🛠️ Tools Used
- Python (pandas, matplotlib)
- PyCharm
- GitHub

## 📦 Dataset
- Source: UCI Machine Learning Repository
- Link: https://archive.ics.uci.edu/dataset/352/online+retail
- Size: 541,909 rows × 8 columns

## 🔍 Key Steps
1. Data Loading & Exploration
2. Data Cleaning (duplicates, nulls, cancelled orders)
3. Feature Engineering (Revenue column)
4. Exploratory Data Analysis
5. Data Visualization

## 📊 Charts Created
| Chart | Description |
|-------|-------------|
| Monthly Revenue Trend | Revenue pattern across 13 months |
| Top 10 Products | Best selling products by quantity |
| Top Countries | Revenue by country |
| Revenue Distribution | Order value spread |

## 💡 Key Insights
1. **November Peak** — November 2011 had highest revenue of £1.5M driven by Black Friday
2. **UK Dominance** — UK contributes ~85% of total revenue
3. **Top Products** — PAPER CRAFT LITTLE BIRDIE leads with 80,000+ units sold
4. **Low Value Orders** — Majority of orders fall between £0–£50
5. **Q4 Seasonality** — Q4 contributes ~40% of annual revenue

## 📈 Key Stats
| Metric | Value |
|--------|-----
| Total Revenue | £10,642,110 |
| Total Orders | 19,960 |
| Total Products | 4,026 |
| Total Countries | 38 |
| Best Month | November 2011 |
| Top Country | United Kingdom |

## 📁 Project Structure
- main.py — Python EDA code
- insights.txt — Key findings
- charts/ — All visualization PNGs
