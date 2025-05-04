mport matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.datasets import copper

data = copper.load_pandas().data

# фильтр по периоду (1961-1970)
filtered_data = data[(data['YEAR'] >= 1961) & (data['YEAR'] <= 1970)]

# построение графиков для рядов
plt.figure(figsize=(12, 6))

plt.plot(filtered_data['YEAR'], filtered_data['WORLDCONSUMPTION'], label='World Consumption')
plt.plot(filtered_data['YEAR'], filtered_data['COPPERPRICE'], label='Copper Price')
plt.plot(filtered_data['YEAR'], filtered_data['ALUMPRICE'], label='Aluminum Price')

plt.title('Динамика показателей меди и алюминия (1961-1970)')
plt.xlabel('Год')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()