#In[0]importacion librerias

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#In[1] importacion de datos csv
#spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_H1.CSV')
spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_Daily.CSV')
#In[2]Munting los datos de stock y agregar dos columnas - MA10 and MA50
spx['MA10'] = spx["CLOSE"].rolling(10).mean()
spx['MA50'] = spx["CLOSE"].rolling(50).mean()
spx = spx.dropna() #usa dropna para remover cualquier "Not a Number" data
spx.head()

#In[3]Agregue la columna "acciones" para tomar decisiones
#añadi la columna "acciones", si MA10>MA50, se coloca un 1 (long one share of stock), si no, se coloca 0 (do nothing)

spx['Acciones'] = [1 if spx.loc[i, 'MA10']>spx.loc[i, 'MA50'] else 0 for i in spx.index]

#In[4]
#Agregue una nueva columna "Beneficio" usando Comprensión de lista, para cualquier fila en spx, si Acciones = 1, el beneficio se calcula como el precio de cierre de
#mañana: el precio de cierre de hoy. De lo contrario, la ganancia es 0.
#Plot a graph to show the Profit/Loss

spx['CLOSETOMORROW'] = spx['CLOSE'].shift(-1)
spx['Profit'] = [spx.loc[i, 'CLOSETOMORROW'] - spx.loc[i, 'CLOSE'] if spx.loc[i, 'Acciones']==1 else 0 for i in spx.index]
spx['Profit'].plot()
plt.axhline(y=0, color='red')

#In[5]Use .cumsum() para mostrar el rendimiento de nuestro modelo si seguimos la estrategia
#Use .cumsum() to calculate the accumulated wealth over the period
spx['Riqueza'] = spx['Profit'].cumsum()
spx.tail()

#In[6]trazar la riqueza para mostrar el crecimiento de las ganancias durante el período

#trazar la riqueza para mostrar el crecimiento de las ganancias durante el período

spx['Riqueza'].plot()
plt.title('El dinero que ganaste es {}'.format(spx.loc[spx.index[-2], 'Riqueza']))