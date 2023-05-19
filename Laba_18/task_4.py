import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('flight_delays.csv', sep=',')
for i in range(1, 13):
    if i in [1, 2, 12]:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Зима'
    elif i in [3, 4, 5]:
        data.loc[data["Month"] == 'c-' + str(i), "Month"] = 'Весна'
    elif i in [6, 7, 8]:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Лето'
    else:
        data.loc[data["Month"] == 'c-'+str(i), "Month"] = 'Осень'
data = data.rename(columns={"Month": "Seasons"})
plot_data = data[data['dep_delayed_15min'] == 'Y'].groupby('Seasons').dep_delayed_15min.count()
plot_data.plot(x='Month', y='count', kind='bar', color='royalblue')
plt.show()