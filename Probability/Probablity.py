import numpy as np
import scipy.stats as stats

# create 6 sided "die"
die_6 = range(1, 7)

# set number of rolls
num_rolls = 5

# roll the "die" the set amount of times
results_1 = np.random.choice(die_6, size = num_rolls, replace = True)
print(results_1)

# create 12-sided "die"
die_12 = range(1,13)

# roll the 12-sided "die" 10 times
results_2 = np.random.choice(die_12, size=10, replace=True)

# PROBABILTY MASS FUNCTION WITH BINOIAL DISTRIBUTION

 value of interest
# change this
x = 3

# sample size
# change this
n = 10

# calculate probability
prob_1 = stats.binom.pmf(x, n, 0.5)
print(prob_1)

## Question 2
prob_2 = stats.binom.pmf(7,20, .5)
print(prob_2)