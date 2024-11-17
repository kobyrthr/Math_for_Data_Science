import numpy as np
import pandas as pd
import codecademylib3

monthly_report = pd.read_csv('monthly_report.csv')

# print(monthly_report.head())

sample_size = len(monthly_report)

print("Sample size is", sample_size)

num_purchased = sum(monthly_report.purchase == 'y')

print("number of purchases is", num_purchased)

#print the head of monthly_report:


#calculate and print sample_size:


#calculate and print num_purchased:
