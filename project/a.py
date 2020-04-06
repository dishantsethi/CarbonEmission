import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("/home/dishantsethi/Development/project/Carbon Emission/project/datasets/annual-co-emissions-by-region.csv")

df = pd.DataFrame(data)
country = df.Entity.unique()
p = df.groupby(['Entity']).sum()

l = list(p.emissions)
df2 = pd.DataFrame(country,l)
print(df2)
