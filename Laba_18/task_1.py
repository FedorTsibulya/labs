import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('flight_delays.csv', sep=',')
for i in range(1,13):
    data.loc[data["Month"] == 'c-'+str(i), "Month"] = i
data_sub_1 = data.groupby('Month').Month.count()
data_sub_2 = data.loc[data['dep_delayed_15min'] == 'Y'].groupby('Month').Month.count()
plot_data = data_sub_1 / data_sub_2
plot_data.plot(x='Month', y='count', kind='bar', color='maroon')
plt.xlabel('Месяц')
plt.ylabel('Доля задержек')
plt.show()
