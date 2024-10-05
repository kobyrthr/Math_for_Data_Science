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