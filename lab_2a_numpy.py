import numpy as np
import pandas as pd

x=np.array([1,2,3,4,5,6,7,8,9,10])

np.arange(10)
a=np.random.random(10)
np.split(x,5)

np.min(x)

np.max(x)

np.average(x)

df=pd.read_csv("president_heights.csv")

height = np.array(df["height(cm)"])

print("minimum height = "+str(np.min(height)))
print("maxmum height = "+str(np.max(height)))
print("average height = "+str(np.average(height)))
