**Retail Demand Forecasting & Inventory Optimization
Project Overview**

Retail Demand Forecasting & Inventory Optimization is a data analytics project designed to help retailers make data-driven inventory decisions by predicting future product demand. The project analyzes historical retail sales data, identifies demand patterns, and forecasts future demand using time-series modeling.

Based on these forecasts, the project calculates optimal inventory planning metrics such as safety stock and reorder point, helping businesses reduce stockouts and minimize excess inventory.

The system integrates Python-based data analysis and forecasting with Power BI dashboards to visualize demand trends, forecast results, and inventory KPIs for decision support.

**Business Problem
**
Retail companies often face two major operational challenges:

Overstocking → Increased holding cost and wasted inventory

Understocking → Lost sales and dissatisfied customers

Accurate demand forecasting combined with inventory planning can help companies maintain optimal stock levels and improve operational efficiency.

**Project Objectives
**
Analyze historical retail sales data

Identify trend, seasonality, and demand volatility

Forecast future demand using time-series models

Calculate optimal safety stock and reorder points

Build a dashboard for demand insights and inventory planning

**Dataset**

The project uses a Global Superstore retail dataset, which contains multi-year transaction data including:

Order Date

Product Category

Quantity Sold

Sales

Customer details

Geographic information

Each row represents a product sold in a customer order transaction.

For this project, the primary variables used were:

Order Date

Category

Quantity

**Project Workflow
****1. Data Preparation
**
Loaded the dataset using Pandas

Converted date fields into proper datetime format

Aggregated transaction data into monthly demand

Structured data for time-series modeling

Output:

Cleaned dataset containing monthly demand per category

**2. Exploratory Data Analysis (EDA)
**
EDA was performed to understand demand patterns before building the forecasting model.

**Key analyses included:
**
Overall demand trends over time

Category-wise demand comparison

Seasonal demand patterns

Demand volatility analysis

**Key findings:
**
Demand showed a clear upward trend

Strong yearly seasonality was observed

Office Supplies category had the highest volatility

**3. Demand Forecasting
**
A SARIMA (Seasonal ARIMA) model was used to forecast future demand.

Model Configuration

SARIMA (1,1,1)(1,1,1,12)

Where:

(1,1,1) → ARIMA component

(1,1,1,12) → Seasonal component with yearly seasonality

Model Evaluation

The dataset was split into:

Training data: 42 months

Testing data: 6 months

Model performance was evaluated using:

MAPE (Mean Absolute Percentage Error)

**Result:
**
Forecast accuracy ≈ 12% MAPE

**4. Demand Forecasting Output
**
The model generated 12-month demand forecasts, which serve as the foundation for inventory planning.

**Output file:
**
**office_supplies_12_month_forecast.csv
****5. Inventory Optimization
**
Using forecasted demand, key inventory planning metrics were calculated.

Average Monthly Demand

Represents expected monthly demand.

Demand Volatility

Measured using standard deviation of historical demand.

Safety Stock

Calculated using:

Safety Stock = Z × σ × √(Lead Time)

Where:

Z = Service level factor

σ = Demand standard deviation

Lead Time = Restocking time

Reorder Point (ROP)

ROP = (Average Demand × Lead Time) + Safety Stock

This determines the inventory level at which new stock should be ordered.

**Dashboard**

An interactive Power BI dashboard was developed to visualize:

Demand Trends

Monthly demand over time

Category comparison

Forecast Visualization

Historical vs predicted demand

Future demand projections

Inventory KPIs

Average demand

Safety stock

Reorder point

The dashboard helps stakeholders quickly understand demand patterns and inventory requirements.

**Tools & Technologies
**
Python
Pandas
NumPy
Matplotlib
Seaborn
Statsmodels (SARIMA)
Scikit-learn
Power BI

**Project Structure
**Retail-Demand-Forecasting
│
├── data
│   ├── raw
│   └── processed
│
├── notebooks
│   ├── 01_data_loading_and_overview.ipynb
│   ├── 02_eda_trend_and_seasonality.ipynb
│   ├── 03_demand_forecasting_sarima.ipynb
│   └── 04_inventory_optimization.ipynb
│
├── outputs
│   ├── forecasts
│   └── reports
│
├── powerbi
│   └── dashboard.pbix
│
├── requirements.txt
└── README.md
**Key Outcomes
**
Built an end-to-end demand forecasting pipeline

Identified seasonal retail demand patterns

Forecasted demand with ~12% prediction error

Designed an inventory planning framework

Developed a business intelligence dashboard for decision support

**Future Improvements
**
Include price and promotion effects

Add region-level demand forecasting

Compare multiple models (Prophet, LSTM)

Build automated inventory recommendation system
