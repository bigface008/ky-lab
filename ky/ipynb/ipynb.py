# %%
import numpy as np
import pandas as pd

data = pd.read_csv("D:\workspace\python\ky-lab\data\data.csv", header=None)

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
