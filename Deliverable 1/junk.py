import pandas as pd
from pandas import DataFrame

emissions = DataFrame()

emissions['Low Altitude'] = [1.50, 1.48, 2.98, 1.40, 3.12, 0.25, 6.73, 5.30, 9.30, 6.96, 7.21, 0.87, 1.06, 7.39, 1.37]
emissions['High Altitude'] = [7.59, 2.06, 8.86, 8.67, 5.61, 6.28, 4.04, 4.40, 9.52, 1.50, 6.07, 7.11, 3.57, 2.68, 1.37]

emissions.to_excel('emissions_from_pandas.xlsx')

emissions_from_excel = pd.read_excel(r'emissions_from_pandas.xlsx')

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

import numpy as np
low_altitude = np.array(emissions_from_excel.iloc[0, :])
high_altitude = np.array(emissions_from_excel.iloc[1, :])

data = (low_altitude, high_altitude)

ax.boxplot(data)
plt.ylabel("Particulate matter (PM) emissions (in g/gal)")
plt.xticks([1, 2], ['Low Altitude', 'High Altitude'])




