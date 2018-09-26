import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun, Times New Roman'

readdata = pd.read_csv('D://data//600000.csv', encoding='gb18030')
readdata.plot()
plt.show()
