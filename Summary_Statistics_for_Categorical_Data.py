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

