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

#simulate one visitor:
one_visitor = np.random.choice(["y","n"],size=1, p=[.1,.9])

print("Did the visitor purchase?:",one_visitor)

#simulate 500 visitors:

simulated_monthly_visitors = np.random.choice(["y","n"],size=500, p=[.1,.9])

print(simulated_monthly_visitors)



null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])
  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)


#calculate the minimum and maximum values in null_outcomes here:

null_min = np.min(null_outcomes)

null_max = np.max(null_outcomes)

print("Max is:",null_max, " and min is:", null_min)

null_outcomes = np.array(null_outcomes)

p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)

print(p_value)


