# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("D:\workspace\python\ky-lab\ky\data\data.csv", header=None)

# %%
data

# %%
slice_len = 75
l1 = data.iloc[0:slice_len]
l2 = data.iloc[slice_len:slice_len * 2]
l3 = data.iloc[slice_len * 2:slice_len * 3]
l4 = data.iloc[slice_len * 3:slice_len * 4]
l5 = data.iloc[slice_len * 4:slice_len * 5]
l6 = data.iloc[slice_len * 5:slice_len * 6]
l7 = data.iloc[slice_len * 6:slice_len * 7]
l8 = data.iloc[slice_len * 7:slice_len * 8]

# %%
l1.iloc[0]

# %%
l1r = l1.iloc[0][::-1]

#%%
l1 = [1, 2, 3]
l2 = l1
l2[1] = 11
print(l1)

#%%
int('123')

#%%
import re
str = 'Get 123 345'
rstr = re.compile(r'^\w{3}\s\d+\s\d+$')
c = rstr.match(str).groups()
print(c)

#%%
import random

#%%
random.randint(0, 10000)

