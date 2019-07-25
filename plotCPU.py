import pandas as pd
import numpy as np
from pandas import Series, DataFrame 
import matplotlib as mb
import matplotlib.pyplot as plt
cpu1_df = pd.read_csv("D:/Anacondadownload/data/node/BCBSAP01/CPU.csv",names=['timestamp','value'])
cpu2_df = pd.read_csv("D:/Anacondadownload/data/node/BCBSAP02/CPU.csv",names=['timestamp','value'])
cpu1_df['timestamp'] = cpu1_df['timestamp'].apply(lambda x:datetime.datetime.fromtimestamp(x))
cpu2_df['timestamp'] = cpu2_df['timestamp'].apply(lambda x:datetime.datetime.fromtimestamp(x))
new_data1 = cpu1_df.query('timestamp<"2018-04-02 00:00"')
new_data2=cpu2_df.query('timestamp<"2018-04-02 00:00"')
plt.figure(figsize=(20,10))
plt.plot(new_data1['timestamp'],new_data1['value'])
plt.plot(new_data2['timestamp'],new_data2['value'])