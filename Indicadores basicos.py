#In[0]importacion librerias

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#In[1] importacion de datos csv
 
spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_H1.CSV')

#In[2]Indicador 1 (diferencia de precios)

#creacion de una columna
spx['Precio 1'] = spx['CLOSE'].shift(-1)
#en este caso se toma el precio de close 1 precio por delante
#fila 1 close=3834 --->precio 1=3830 (el valor de close anterior)}

#ahora vamos a sacar la diferencia de precios
#price diference=(close price of tomorrow-close price of today)
spx['diferencia de precio']=spx['Precio 1']-spx['CLOSE']
spx.head(100) #se comprueba

#In[3]indicador 2 (Daily return)

#Daily return= price diference/close price today
spx['Dreturn']=spx['diferencia de precio']/spx['CLOSE']
spx.head(100) #se comprueba

#In[4]indicador 3 (direccion)
"""
primero se aplican las siguientes reglas
si diferencia de precio>0  ----> up(1)
si diferencia de precio<0  ----> down(-1)
"""
#se usa list compresion
spx['direccion']=[1 if spx['diferencia de precio'].loc[i] > 0 else 0 for i in spx.index]
#                                                                    ^[dominio donde se hace la operacion]
"""
Explicando lo que se hizo arriba se puede decir que si es mayor que 1 cualquier valor en 
diferencia de precio se coloca un 1 en price direccion y si no se coloca un 0
"""
spx.head(100) #se comprueba
#print('diferencia de precio en {} es {}. en la direccion {}'.format('03.01.2023', spx['diferencia de precio'].loc['03.01.2023'], spx['Direction'].loc['30.01.2023']))
#la linea de arriba da error porque no se convirtieron fechas

#In[5]indicador 4 (medias moviles)

"""Crear una nueva columna en Data frame
usando Rolling Window calculation (.rolling()) - Moving average"""
spx['ma50'] = spx['CLOSE'].rolling(50).mean()

#ahora vamos a graficarla
plt.figure(figsize=(10, 8))
spx['ma50'].plot(label='MA50')
#para usar .loc['2015-01-01':'2015-12-31'] toca convertir las fechas
spx['CLOSE'].plot(label='Close')
plt.legend()
plt.show()
