import pandas as pd

from matplotlib import pyplot, rc

data = pd.read_csv('data\\data2.csv', skiprows=4, index_col='Country Name')
print data.shape
print data['Country Code']
ausData = data[data['Country Code'] == 'AUS']
print ausData.shape
print ausData['1960']
font = {'family':'Courier New'}
rc('font', **font)
pyplot.style.use('Solarize_Light2')
selected_year = ['1960', '1970', '1980', '1990']
ausData.plot(kind='bar', y=selected_year, fontsize=20)
print pyplot.style.available
pyplot.show()
