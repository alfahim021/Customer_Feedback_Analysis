# Customer Feedback Analysis Dashboard

## Overview

This project analyzes customer feedback data using sentiment analysis to gain insights that help improve product quality and customer satisfaction.

It uses Python (NLTK, TextBlob, Pandas) for data processing and Tableau for building interactive dashboards.

---

## Project Structure

Customer_Feedback_Analysis
│
├── data
│ ├── raw\ # Original datasets
│ ├── processed\ # Cleaned and labeled datasets
│
├── notebooks\ # Jupyter notebooks for analysis
│
├── scripts\ # Python scripts for data processing
│
├── reports\ # Reports and presentations
│
├── tableau_dashboard\ # Tableau dashboard files (.twbx)
│
├── README.md # Project overview and instructions
└── requirements.txt # Python package dependencies





## Setup and Usage

### Prerequisites

- Python 3.7 or higher installed
- Required Python packages (listed in `requirements.txt`)

### Install Packages

Open **Command Prompt** and run:

pip install -r requirements.txt


### Run Data Processing Script

1. Place your raw data file (`Customer_Feedback.csv`) inside:

data\raw\


2. Run the analysis script by executing:

python scripts\feedback_analysis.py

kotlin
Copy

This will generate cleaned and sentiment-labeled data in:

data\processed\


### Use Tableau Dashboard

- Open Tableau Desktop.
- Load the dashboard file located at:

tableau_dashboard\Customer_Feedback_Dashboard.twbx

Explore interactive visualizations of customer sentiments and feedback trends.

---

## Contact

**Your Name**  
Email: alfahim021@gmail.com  
