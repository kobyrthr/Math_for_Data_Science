import scipy.stats as stats
import numpy as np

## For checkpoints 1 and 2
# 5000 draws, lambda = 7
rand_vars_7 = stats.poisson.rvs(7, size = 5000)

## Checkpoint 1
# print variance of rand_vars_7
print(np.var(rand_vars_7))


## Checkpoint 2
# print minimum and maximum of rand_vars_7
print(np.min(rand_vars_7),np.max(rand_vars_7))

## For checkpoints 3 and 4
# 5000 draws, lambda = 17
rand_vars_17 = stats.poisson.rvs(17, size = 5000)

## Checkpoint 3
# print variance of rand_vars_17
print(np.var(rand_vars_17))

## Checkpoint 4
# print minimum and maximum of rand_vars_17
print(np.min(rand_vars_17),np.max(rand_vars_17))


import scipy.stats as stats
import numpy as np

## Checkpoint 1
expected_bonus = 75000*.08
print(expected_bonus)


## Checkpoint 2
num_goals = stats.poisson.rvs(4, size=100)


## Checkpoint 3
print(np.var(num_goals))

## Checkpoint 4
num_goals_2 = num_goals*2
print(np.var(num_goals_2))