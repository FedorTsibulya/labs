import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('flight_delays.csv')
data_sub_1 = data.groupby('Origin').Dest.count()
data_sub_2 = data.loc[data['dep_delayed_15min'] == 'Y'].groupby('Origin').Dest.count()
plot_data = data_sub_2 / data_sub_1
plot_data = plot_data.reset_index(name='Доля задержек').sort_values('Доля задержек', ascending=False).head(10)
plot_data.plot(x='Origin', y='Доля задержек', kind='bar', color='goldenrod')
plt.xlabel('Аэропорт')
plt.show()