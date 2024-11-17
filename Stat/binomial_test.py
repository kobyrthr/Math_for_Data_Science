import numpy as np
import pandas as pd
import codecademylib3
from scipy.stats import binom_test

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

def simulation_binomial_test(observed_successes,n,p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

# Using the binom_test function from scipy


p_value_2sided= binom_test(41, n=500, p=.1)

print(p_value_2sided)
# calculate p_value_1sided here:

p_value_1sided = binom_test(41, n=500, p=.1,alternative = 'less')

print(p_value_1sided)

