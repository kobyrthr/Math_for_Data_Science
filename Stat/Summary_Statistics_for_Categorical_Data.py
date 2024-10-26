import codecademylib3
import pandas as pd

nyc_trees = pd.read_csv("./nyc_tree_census.csv")


# Show the first few rows of nyc_trees
print(nyc_trees.head)
# Which columns are categorical vars?
categorical_vars = ["neighborhood","status","health","spc_common"]

# NOMINAL CATEGORIES
import pandas as pd

# Read NYC Trees Data
nyc_trees = pd.read_csv("./nyc_tree_census.csv")

# Get tree counts by neighborhood
tree_counts=nyc_trees["neighborhood"].value_counts()

print(tree_counts)

# Get neighborhoods with most trees
greenest_neighborhood = (tree_counts.index[0])

print(greenest_neighborhood)

# Binary Categorical Variable: Frequency and Proportion

import pandas as pd
import numpy as np

# Get NYC Trees Data
df = pd.read_csv('nyc_tree_census.csv')

living_frequency = (df.status=='Alive').sum()

living_proportion = (df.status=='Alive').mean()

print("living_proportion=",living_proportion,"living_frequency=",living_frequency)

giant_frequency = (df.trunk_diam > 30).sum()

giant_proportion = (df.trunk_diam > 30).mean()

print("giant_proportion =",giant_proportion,"giant_frequency =",giant_frequency)

# Summarizing Automobile Evaluation Data

import pandas as pd
import numpy as np

df = pd.read_csv('car_eval_dataset.csv')
print(df.head())

#count country frequencies
print(df.manufacturer_country.value_counts())

#print top country
print(df.manufacturer_country.value_counts().index[0])

#print 4th most frequent country
print(df.manufacturer_country.value_counts().index[3])

#print country proportions
print(df.manufacturer_country.value_counts(normalize=True))

#print country proportions
print(df.manufacturer_country.value_counts(normalize=True))

#print Japan's proportion
print(df.manufacturer_country.value_counts(normalize=True)['Japan'])

#print out possible 'buying cost' vairables
print(df.buying_cost.unique())

#buying costs ordered
buying_cost_categories = ['low','med','high','vhigh']

#make buying_cost a category type
df.buying_cost  = pd.Categorical(df.buying_cost,buying_cost_categories,ordered=True)

#Median of buying cost
med_buying_cost_index = np.median(df.buying_cost.cat.codes)

median_buying_cost = buying_cost_categories[int(med_buying_cost_index)]

print(median_buying_cost)


#print proportions of luggage
print(df.luggage.value_counts(normalize=True,dropna=False))

#print count no. of cars with >=5 doors
print(df.doors.value_counts()['5more'])

#print proportion of cars that have >=5 doors
print(df.doors.value_counts(normalize=1,dropna=0)['5more'])


