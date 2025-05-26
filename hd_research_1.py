# import necessary libraries
import pandas as pd
import numpy as np

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
chol_hd = yes_hd['chol']
print()

# task 2: Calculate the mean cholesterol level for patients who were diagnosed with heart disease
mean_chol_hd = np.mean(chol_hd)
print(f'Mean cholesterol level for patients with heart disease: {mean_chol_hd:.2f}')
print("This level is higher than 240 mg/dl and and therefore unhealthy.")
print()