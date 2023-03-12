#In[0]importamos librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#In[1]

spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_Daily.CSV')
spx.head()


#In[2] Distribución de retorno logarítmico
# vamos a jugar con los datos de ms calculando el retorno logarítmico
spx['LogReturn'] = np.log(spx['CLOSE']).shift(-1) - np.log(spx['CLOSE'])

#In[3] Trazar un histograma para mostrar la distribución del rendimiento logarítmico de las acciones de SPX.
# Puedes ver que está muy cerca de una distribución normal
from scipy.stats import norm
mu = spx['LogReturn'].mean() #media
sigma = spx['LogReturn'].std(ddof=1) #desviacion estandar

density = pd.DataFrame() 
density['x'] = np.arange(spx['LogReturn'].min()-0.01, spx['LogReturn'].max()+0.01, 0.001) #curva de densidad de probabilidad normal
density['pdf'] = norm.pdf(density['x'], mu, sigma) #distribución normal
"""density contiene un rango de valores de retorno logarítmico 
y su correspondiente densidad de probabilidad de una distribución normal"""

spx['LogReturn'].hist(bins=50, figsize=(15, 8))
plt.plot(density['x'], density['pdf'], color='red')
plt.show()

#In[4]probabilidad de que el precio de las acciones caiga un cierto porcentaje en un día
# probabilidad de que el precio de las acciones de spx caiga más del 5% en un día
prob_return1 = norm.cdf(-0.05, mu, sigma)
"""calcula la probabilidad de un retorno logarítmico diario sea igual o menor 
que un valor dado utilizando la función de distribución acumulativa
 de una distribución normal con media "mu" y desviación estándar sigma"""
print('la probabilidad es ', prob_return1)

#In[5]Calcule la probabilidad de que el precio de las acciones caiga en un cierto porcentaje en un año
# drop over 40% in 220 days
mu220 = 220*mu
sigma220 = (220**0.5) * sigma
print('La probabilidad de caer mas de un 40% en 220 dias es ', norm.cdf(-0.4, mu220, sigma220))
#In[6]Calcular valor en riesgo (VaR)
# valor en riesgo (VaR)
VaR = norm.ppf(0.05, mu, sigma)
print('Valor de un solo día en riesgo ', VaR)
# Quatile 
# 5% quantile
print('5% quantile ', norm.ppf(0.05, mu, sigma))
# 95% quantile
print('95% quantile ', norm.ppf(0.95, mu, sigma))

# This is your turn to calcuate the 25% and 75% Quantile of the return
# 25% quantile
q25 = norm.ppf(0.25, mu, sigma)
print('25% quantile ', q25)
# 75% quantile
q75 = norm.ppf(0.75, mu, sigma) 
print('75% quantile ', q75)
