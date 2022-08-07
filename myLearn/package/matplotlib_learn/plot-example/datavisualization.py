import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
print(__name__)
print(__file__)

print(os.getcwd())

df_can = pd.read_excel('Canada.xlsx',
                       sheet_name = 'Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter = 2,engine='openpyxl')
df_can.drop(['AREA','REG','DEV','Type','Coverage'],
            axis =1,
            inplace = True)

df_can.rename(columns={'OdName': 'Country',
                       'AreaName': 'Continent', 
                       'RegName': 'Region'}, 
              inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.set_index('Country',inplace=True)
# print(df_can.head())
df_can.columns = list(map(str, df_can.columns))
years = list(map(str,range(1980,2014)))
# print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
# passing in years 1980 - 2013 to exclude the 'total' column

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# dataset = df_can.loc[['India','China'], years]
dataset = df_can.head(5)
dataset = dataset[years].transpose()

# let's change the index values of Haiti to type integer for plotting
# dataset = dataset.transpose()

dataset.index = dataset.index.map(int)
dataset.plot(kind='bar')
plt.title(f'Immigration from {dataset.columns.tolist()}')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
# plt.text(2000, 6000, '2010 Earthquake')  # see note below
plt.show()  # need this line to show the updates made to the figure



