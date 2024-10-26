import scipy.stats as stats
import codecademylib3

from histogram_function import histogram_function

## Checkpoint 1
# calculate prob_15
prob_15 = stats.poisson.pmf(15,15)

print (prob_15)


## Checkpoint 
# calculate prob_7_to_9
prob_7_to_9 = stats.poisson.pmf(9,15) + stats.poisson.pmf(8,15) + stats.poisson.pmf(7,15)

print (prob_7_to_9)

## Checkpoint 1
# calculate prob_more_than_20
prob_more_than_20 = 1 - stats.poisson.cdf(20,15)

print (prob_more_than_20)

## Checkpoint 
# calculate prob_17_to_21
prob_17_to_21 = stats.poisson.cdf(21,15) - stats.poisson.cdf(16,15)

print (prob_17_to_21)

## Checkpoint 1
# lambda = 15, 1000 random draws 
rand_vars = stats.poisson.rvs(15, size = 1000)


## Checkpoint 2
# print the mean of rand_vars
print(rand_vars.mean())


## Checkpoint 3
histogram_function(rand_vars)

