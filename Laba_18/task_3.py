import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = plt.get_cmap('Greens')(np.linspace(0.2, 0.7, 5))

data = pd.read_csv('flight_delays.csv', sep=',')
data_sub_1 = data[data['dep_delayed_15min'] == 'Y'].groupby('Dest').dep_delayed_15min.count()
plot_data = data_sub_1.nlargest(5)
plot_data.plot(kind='pie', colors=colors, wedgeprops={"linewidth": 1, "edgecolor": "white"})
plt.ylabel('Топ направлений по задержкам')
plt.show()