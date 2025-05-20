# Customer Feedback Analysis Dashboard

## Overview

This project analyzes customer feedback data collected from multiple sources using sentiment analysis techniques. The goal is to extract actionable insights to improve product quality and customer satisfaction.

The analysis uses Python (NLTK, TextBlob, Pandas) for data cleaning and sentiment classification, and Tableau for interactive data visualization and dashboard creation.

---

## Project Structure

Customer_Feedback_Analysis/
│
├── data/
│ ├── raw/ # Original raw datasets
│ ├── processed/ # Cleaned datasets with sentiment labels
│
├── notebooks/ # Jupyter notebooks for analysis and prototyping
│
├── scripts/ # Python scripts for preprocessing and analysis
│
├── reports/ # Weekly summary reports and presentations
│
├── tableau_dashboard/ # Tableau workbook files (.twbx)
│
├── README.md # This file: project overview and instructions
├── requirements.txt # Python dependencies



## Setup and Usage

### Requirements

- Python 3.7 or above
- Packages listed in `requirements.txt` (install with pip)

```bash
pip install -r requirements.txt
Run Data Analysis
Place your raw dataset (redmi6.csv) in data/raw/.

Run the Python script to clean data and perform sentiment analysis:

bash
Copy
python scripts/feedback_analysis.py
This generates cleaned and sentiment-labeled files in data/processed/.

Tableau Dashboard
Open the Tableau workbook in tableau_dashboard/Customer_Feedback_Dashboard.twbx to explore interactive dashboards built on processed data.

Contact
For questions or help, email: alfahim021@gmail.com
