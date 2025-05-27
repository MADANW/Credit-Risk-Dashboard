import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter 
import math

# Load the data
data = pd.read_csv('credit.csv')
data['default'] = data['default'].map({'yes': 1, 'no': 0})
data.replace("unknown", "Missing", inplace=True)
bins = [0, 25, 40, 60, 100]
labels = ['Young', 'Adult', 'Middle Age', 'Senior']
data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels)
data['loan_to_income'] = data['amount'] / data['percent_of_income']
data['risk_flag'] = data.apply(lambda row: 'High Risk' if (row['savings_balance'] == '< 100 DM' and row['checking_balance'] == '< 0 DM') else 'Normal', axis=1)

#data.to_csv('credit_cleaned.csv', index=False)

with pd.ExcelWriter("credit_cleaned.xlsx", engine='xlsxwriter') as writer:
    data.to_excel(writer, sheet_name='CleanedData', index=False)

# Display basic info about the cleaned dataset
print("Dataset shape:", data.shape)
print("\nNew columns created:")
print("- age_group:", data['age_group'].value_counts())
print("- risk_flag:", data['risk_flag'].value_counts())
print("- default (encoded):", data['default'].value_counts())
print("\n✅ Excel file 'credit_cleaned.xlsx' created successfully!")