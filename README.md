# Credit Risk & Loan Behavior Dashboard

## 📊 Project Overview

A comprehensive data analysis and visualization project that explores credit risk patterns and customer loan behavior using real financial data from 1,000 anonymized bank clients. This dashboard provides actionable insights for banking industry decision-makers to identify high-risk profiles, understand spending trends, and optimize loan approval processes.

**🎯 Business Impact**: This analysis reveals that high-risk customers have a **52.1% default rate** compared to **23.8%** for normal-risk customers, enabling banks to potentially reduce loan losses by improving risk assessment criteria.

## 🔍 Key Findings & Insights

### 📈 **Critical Risk Metrics**
- **Overall Default Rate**: 30.0% (300 out of 1,000 customers)
- **High-Risk Customer Identification**: 21.9% of portfolio flagged as high-risk
- **Risk Validation**: High-risk customers default at **2.2x higher rate** than normal customers
- **Average Loan Amount**: 3,271 DM with 20.9 months average duration

### 👥 **Customer Demographics**
- **Adults (25-40)**: 53.6% of customer base - largest segment
- **Middle Age (40-60)**: 22.9% of customers
- **Young (<25)**: 19.0% of customers  
- **Seniors (60+)**: 4.5% of customers

### 💰 **Loan Purpose Risk Analysis**
**Highest Risk Loan Categories:**
1. **Car0**: 41.7% default rate (specialized vehicle loans)
2. **Education**: 39.0% default rate (student/training loans)
3. **Renovations**: 36.4% default rate (home improvement)
4. **Business**: 35.1% default rate (commercial loans)
5. **Car**: 31.5% default rate (standard auto loans)

### 🚨 **Risk Factors Identified**
- **Low Account Balances**: Customers with savings < 100 DM AND checking < 0 DM
- **High Loan-to-Income Ratios**: Average ratio of 1,543.5 indicates potential overextension
- **Purpose-Based Risk**: Education and business loans show elevated default rates

## 🎯 Objectives

- **Risk Assessment**: Identify customer profiles most likely to default on loans
- **Behavioral Analysis**: Analyze spending and repayment patterns across different customer segments
- **Business Intelligence**: Provide actionable insights for financial decision-making
- **Data Visualization**: Create interactive dashboards for stakeholder communication

## 📂 Dataset Information

- **Source**: `credit.csv` (1,000 customer records)
- **Features**: 20 total columns (17 original + 3 engineered)
- **Target Variable**: Default status (30% positive class)
- **Data Quality**: Successfully processed with minimal missing values

**Original Features:**
- Financial metrics (loan amount, income %, account balances)
- Demographics (age, job, housing status)
- Credit history and loan details
- Default status (target variable)

**Engineered Features:**
- Age groups (Young, Adult, Middle Age, Senior)
- Loan-to-income ratio
- Risk flag (High Risk vs Normal)

## 🛠 Technology Stack

- **Data Analysis**: Python (Pandas, NumPy)
- **Visualization**: Matplotlib, Seaborn
- **Dashboard**: Power BI Desktop
- **Data Export**: Excel (xlsxwriter)
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
   pip install pandas numpy matplotlib seaborn xlsxwriter
   ```

4. **Run data processing**
   ```bash
   python script.py
   ```

5. **Generate insights**
   ```bash
   python analysis.py
   ```

## 📁 Project Structure

```
creditreportdash/
├── credit.csv                    # Original dataset (1,000 records)
├── credit_cleaned.csv           # Processed dataset for analysis
├── credit_cleaned.xlsx          # Excel format for Power BI
├── CustomerSurvey_RiskReport.pbix # Power BI dashboard file
├── script.py                    # Data cleaning and preprocessing
├── analysis.py                  # Detailed insights generation
├── README.md                    # This documentation
├── myenv/                       # Virtual environment
└── .gitignore                   # Git ignore rules
```

## 🔧 Data Processing Pipeline

The `script.py` performs the following transformations:

1. **Binary Encoding**: Convert 'yes/no' to 1/0 for default column
2. **Missing Value Handling**: Replace 'unknown' with 'Missing'
3. **Age Categorization**: Create age groups (Young, Adult, Middle Age, Senior)
4. **Feature Engineering**: 
   - **Loan-to-income ratio**: `amount / percent_of_income`
   - **Risk flag**: High-risk if savings < 100 DM AND checking < 0 DM
5. **Export**: Generate both CSV and Excel formats for analysis

## 📊 Dashboard Components

### 1. **Executive Summary**
- Key KPIs: 30% default rate, 21.9% high-risk customers
- Portfolio overview: 1,000 customers, 3,271 DM average loan
- Risk distribution across customer segments

### 2. **Credit Risk Analysis**
- Risk trends by demographics and financial profiles
- High-risk vs normal customer comparison (52.1% vs 23.8% default rates)
- Account balance impact on default probability

### 3. **Loan Purpose Analysis**
- Default rates by loan purpose (Education: 39%, Business: 35.1%)
- Risk assessment for different loan categories
- Portfolio composition and risk distribution

### 4. **Customer Segmentation**
- Age group analysis (Adults: 53.6% of portfolio)
- Interactive filtering by customer attributes
- Demographic risk patterns

## 💡 Business Recommendations

### 🎯 **Immediate Actions**
1. **Enhanced Screening**: Implement stricter criteria for education and business loans
2. **Account Balance Requirements**: Consider minimum balance thresholds for loan approval
3. **Risk-Based Pricing**: Adjust interest rates based on identified risk factors


## 🔍 Technical Insights

- **Data Quality**: 100% data completeness after preprocessing
- **Feature Engineering**: 3 new variables significantly improve risk identification
- **Risk Segmentation**: Binary risk flag achieves 2.2x separation in default rates
- **Scalability**: Pipeline designed for larger datasets and real-time processing

## 📝 Usage

1. **Data Exploration**: Run `script.py` to process and explore the dataset
2. **Insights Generation**: Run `analysis.py` for detailed statistical analysis
3. **Power BI Dashboard**: Load `credit_cleaned.xlsx` into Power BI Desktop
4. **Business Analysis**: Use findings for risk management and loan policy decisions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/analysis-enhancement`)
3. Commit changes (`git commit -am 'Add new analysis feature'`)
4. Push to branch (`git push origin feature/analysis-enhancement`)
5. Create Pull Request

## 📊 Data Dictionary

| Column | Description | Type | Sample Values |
|--------|-------------|------|---------------|
| checking_balance | Current account balance range | Categorical | "< 0 DM", "1 - 200 DM" |
| months_loan_duration | Loan duration in months | Numeric | 6-72 months |
| credit_history | Credit history status | Categorical | "good", "poor", "critical" |
| purpose | Loan purpose | Categorical | "car", "education", "business" |
| amount | Loan amount in DM | Numeric | 250-18,424 DM |
| savings_balance | Savings account balance range | Categorical | "< 100 DM", "> 1000 DM" |
| employment_duration | Employment length | Categorical | "< 1 year", "> 7 years" |
| percent_of_income | Loan as % of income | Numeric | 1-4% |
| age | Customer age | Numeric | 19-75 years |
| default | Loan default status (target) | Binary | 0 (no), 1 (yes) |
| **age_group** | Age category (derived) | Categorical | Young, Adult, Middle Age, Senior |
| **loan_to_income** | Loan amount / income % (derived) | Numeric | Calculated ratio |
| **risk_flag** | High risk indicator (derived) | Binary | "High Risk", "Normal" |

## 📅 Project Timeline

- [x] Data exploration and understanding
- [x] Data cleaning and preprocessing  
- [x] Feature engineering and risk factor identification
- [x] Statistical analysis and insights generation
- [x] Power BI dashboard development
- [x] Business recommendations documentation
- [x] Technical documentation completion

## 📧 Contact

For questions or collaboration opportunities, please reach out through the repository issues or discussions.

## 📄 License

This project is for educational and portfolio purposes. Please ensure compliance with data privacy regulations when using similar datasets.

---

*Last updated: May 2025*
*Dashboard Status: ✅ Complete with actionable business insights* 