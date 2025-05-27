# import necessary libraries
import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, binomtest

# load and inspect the dataset
hd = pd.read_csv('heart_disease.csv', sep=',')
print()
print(hd.shape)
print(hd.head())
print()
print(hd.columns)
print()
# print(hd.info())
# print(hd.describe())

# split data into two subsets
yes_filter = (hd['heart_disease'] == 'presence')
no_filter = (hd['heart_disease'] == 'absence')

yes_hd = hd.loc[yes_filter]
no_hd = hd.loc[no_filter]

# task 1: save cholesterol levels for patients with heart disease
yes_chol_hd = yes_hd['chol']
print()

# task 2: Calculate the mean cholesterol level for patients who were diagnosed with heart disease
mean_chol_hd = np.mean(yes_chol_hd)
print(f'Mean cholesterol level for patients with heart disease: {mean_chol_hd:.2f}')
print("This level is higher than 240 mg/dl and and therefore unhealthy.")
print()

# task 3: Implementing a One-Sample T-Test
# hypotheses:
# H0: The mean cholesterol level for patients with heart disease is equal to 240 mg/dl
# H1: The mean cholesterol level for patients with heart disease is greater than 240 mg/dl

_, p_value = ttest_1samp(yes_chol_hd, 240.00)
print(f'Two sides p-value for the one-sample t-test for patients with heart disease: {p_value:.4f}')
print(f"One-sided p-value for the one-sample t-test for patients with heart disease: {p_value / 2:.4f}")

# task 4: Interpret the results
print("Using a significance threshold of 0.05 we can conclude that the mean cholesterol level for patients with heart disease is significantly higher than 240 mg/dl.")

# task 5: step 1-4 for patients without heart disease
no_chol_hd = no_hd['chol']
print()
mean_chol_hd = np.mean(no_chol_hd)
print(f'Mean cholesterol level for patients without heart disease: {mean_chol_hd:.2f}')
print("This level is greater than 240 mg/dl and therefore also unhealthy.")
print()
_, p_value = ttest_1samp(no_chol_hd, 240.00)
print(f'Two sides p-value for the one-sample t-test for patients without heart disease: {p_value:.4f}')
print(f"One-sided p-value for the one-sample t-test for patients without heart disease: {p_value / 2:.4f}")
print("Using a significance threshold of 0.05 we can conclude that the mean cholesterol level for patients without heart disease is significantly lower than 240 mg/dl.")
print()

# task 6: Save the number of patients
num_patients = len(hd)
print(f"The number of patients is: {num_patients}")
print()

# task 7: Calculate the number of patients with fasting blood sugar (fbs) greater than 120
num_highfbs_patients = np.sum(hd['fbs'] == 1.0)
print(f"The number of patients with fasting blood sugar (fbs) greater than 120 is: {num_highfbs_patients}")
print()
# with filtering
# filt_fbs = (hd['fbs'] == 1.0)
# print(len(hd[filt_fbs]))

# task 8: estimated number of people with diabetes (8%)
est_diabetes = 0.08 * num_patients
print(f"The estimated number of people with diabetes: {est_diabetes:.0f}")
print()

# task 9-10: implement a binomial test
p_value = binomtest(num_highfbs_patients, n=num_patients, p=0.08, alternative='greater')
print(f"The p-value: {p_value.pvalue:.6f}")
print("This p-value is less than 0.05, indicating that this sample likely comes from a population where more than 8% of people have fbs > 120 mg/dl.")