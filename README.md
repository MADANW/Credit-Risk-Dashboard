# Credit Risk & Loan Behavior Dashboard

## 📊 Project Overview

A comprehensive data analysis and visualization project focused on exploring credit risk patterns and customer loan behavior. This project analyzes financial data from 1,000 anonymized clients to identify high-risk profiles, spending trends, and repayment behaviors for banking industry decision-makers.

## 🎯 Objectives

- **Risk Assessment**: Identify customer profiles most likely to default on loans
- **Behavioral Analysis**: Analyze spending and repayment patterns across different customer segments
- **Business Intelligence**: Provide actionable insights for financial decision-making
- **Data Visualization**: Create interactive dashboards for stakeholder communication

## 📂 Dataset Information

- **Source**: `credit.csv` (1,000 customer records)
- **Features**: 17 original columns including:
  - Financial metrics (loan amount, income %, account balances)
  - Demographics (age, job, housing status)
  - Credit history and loan details
  - Default status (target variable)

## 🛠 Technology Stack

- **Data Analysis**: Python (Pandas, NumPy)
- **Visualization**: Matplotlib, Seaborn
- **Dashboard**: Power BI
- **Version Control**: Git/GitHub
- **Environment**: Virtual Environment (myenv)

## 📋 Prerequisites

- Python 3.8+
- Power BI Desktop
- Git

## 🚀 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd creditreportdash
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

4. **Run data processing**
   ```bash
   python script.py
   ```

## 📁 Project Structure

```
creditreportdash/
├── credit.csv              # Original dataset
├── credit_cleaned.csv      # Processed dataset for Power BI
├── script.py              # Data cleaning and preprocessing
├── project_overview.txt   # Project planning document
├── instructions.txt       # Data cleaning guidelines
├── README.md             # This file
├── myenv/                # Virtual environment
└── .gitignore           # Git ignore rules
```

## 🔧 Data Processing Pipeline

The `script.py` performs the following transformations:

1. **Binary Encoding**: Convert 'yes/no' to 1/0 for default column
2. **Missing Value Handling**: Replace 'unknown' with 'Missing'
3. **Age Categorization**: Create age groups (Young, Adult, Middle Age, Senior)
4. **Feature Engineering**: 
   - Loan-to-income ratio calculation
   - High-risk customer flagging
5. **Export**: Generate `credit_cleaned.csv` for Power BI

## 📊 Key Features Created

- **Age Groups**: Categorical age segments for demographic analysis
- **Loan-to-Income Ratio**: Financial burden assessment metric
- **Risk Flag**: Binary indicator for high-risk customers
- **Default Encoding**: Numerical target variable for modeling

## 📈 Dashboard Components (Planned)

1. **Executive Summary**: Key KPIs and overview metrics
2. **Credit Risk Analysis**: Risk trends by demographics and financials
3. **Spending & Repayment**: Loan behavior and payment patterns
4. **Customer Segmentation**: Interactive filtering by customer attributes

## 🔍 Key Insights (To Be Updated)

- Default rate: 30% (300 out of 1,000 customers)
- High-risk customers: 21.9% of total portfolio
- Age distribution: Adults (25-40) represent 53.6% of customers
- Risk correlation with account balances and loan amounts

## 📝 Usage

1. **Data Exploration**: Run `script.py` to process and explore the dataset
2. **Power BI Dashboard**: Load `credit_cleaned.csv` into Power BI Desktop
3. **Analysis**: Use the cleaned data for further statistical analysis
4. **Reporting**: Generate insights and recommendations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-enhancement`)
3. Commit changes (`git commit -am 'Add new analysis feature'`)
4. Push to branch (`git push origin feature/analysis-enhancement`)
5. Create Pull Request

## 📊 Data Dictionary

| Column | Description | Type |
|--------|-------------|------|
| checking_balance | Current account balance range | Categorical |
| months_loan_duration | Loan duration in months | Numeric |
| credit_history | Credit history status | Categorical |
| purpose | Loan purpose | Categorical |
| amount | Loan amount | Numeric |
| savings_balance | Savings account balance range | Categorical |
| employment_duration | Employment length | Categorical |
| percent_of_income | Loan as % of income | Numeric |
| age | Customer age | Numeric |
| default | Loan default status (target) | Binary |
| age_group | Age category (derived) | Categorical |
| loan_to_income | Loan amount / income % (derived) | Numeric |
| risk_flag | High risk indicator (derived) | Binary |

## 📅 Project Timeline

- [x] Data exploration and understanding
- [x] Data cleaning and preprocessing
- [x] Feature engineering
- [ ] Power BI dashboard development
- [ ] Insights documentation
- [ ] Final presentation preparation

## 📧 Contact

For questions or collaboration opportunities, please reach out through the repository issues or discussions.

## 📄 License

This project is for educational and portfolio purposes. Please ensure compliance with data privacy regulations when using similar datasets.

---

*Last updated: May 2025* 