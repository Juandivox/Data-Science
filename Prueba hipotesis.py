#In[0] importamos librerias
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#In[1] importar SP500.csv y agregar una nueva función: retorno logaritmico
spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_Daily.csv')
spx['logReturn'] = np.log(spx['CLOSE'].shift(-1)) - np.log(spx['CLOSE'])

#In[2]retorno logaritmico sube y baja durante el período
spx['logReturn'].plot(figsize=(20, 8))
plt.axhline(0, color='red')
plt.show()

#In[3]Pasos involucrados en la prueba de una afirmación mediante la prueba de hipótesis
#Paso 1: Establecer hipótesis
#H0:μ=0    Ha:μ≠0
#H0 significa que el rendimiento promedio de las acciones es 0 H1 significa que el rendimiento promedio de las acciones no es igual a 0

#In[]Paso 2: Calcular el estadístico de prueba
sample_mean = spx['logReturn'].mean()
sample_std = spx['logReturn'].std(ddof=1)
n = spx['logReturn'].shape[0]

# si el tamaño de la muestra n es lo suficientemente grande, podemos usar la distribución z, en lugar de la distribución t
# mu = 0 bajo la hipótesis nula

zhat = (sample_mean - 0)/(sample_std/n**0.5)
print(zhat)
#In[]Paso 3: Establecer criterios de decisión
# nivel de confianza
alpha = 0.05

zleft = norm.ppf(alpha/2, 0, 1)
zright = -zleft  # la distribución z es simétrica
print(zleft, zright)

#In[]Paso 4: Tomar una decisión: ¿rechazaremos H0?
print('En un nivel significativo de {}, vamos a rechazar: {}'.format(alpha, zhat>zright or zhat<zleft))
