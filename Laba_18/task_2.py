import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('flight_delays.csv', sep=',')
plot_data = data[data['dep_delayed_15min'] == 'Y'].groupby('Distance').Distance.count()
plot_data.plot(kind='line', x='Distance', y='count', color='teal')
plt.xlabel('Длина пути')
plt.ylabel('Количество задержек')
plt.show()