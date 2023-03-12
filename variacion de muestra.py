
#In[0]importacion de librerias / Variation of Sample
import pandas as pd
import numpy as np
from scipy.stats import norm

#In[1]La media muestral y la desviación estándar siguen cambiando, pero siempre dentro de un cierto rango
Fstsample = pd.DataFrame(np.random.normal(10, 5, size=30))
print('sample mean is ', Fstsample[0].mean())
print('sample SD is ', Fstsample[0].std(ddof=1))

#In[2] Distribución empírica de la media
meanlist = []
for t in range(10000):
    sample = pd.DataFrame(np.random.normal(10, 5, size=30))
    meanlist.append(sample[0].mean())

#In[3]crea la columna meanlist
collection = pd.DataFrame()
collection['meanlist'] = meanlist

#In[4] crea un histograma bins indica que se dividan los valores entre ese valor
collection['meanlist'].hist(bins=100, density=1,figsize=(15,8))

#In[5]Muestreo de distribución arbitraria
# Vea lo que le dice el teorema del límite central... el tamaño de la muestra es lo suficientemente grande,
# la distribución de la media muestral es aproximadamente normal
# apop no es normal, pero intente cambiar el tamaño de la muestra de 100 a un número mayor. La distribución de la media muestral de apop
# se normaliza.
sample_size = 100
samplemeanlist = []
apop =  pd.DataFrame([1, 0, 1, 0, 1])
for t in range(10000):
    sample = apop[0].sample(sample_size, replace=True)  # small sample size
    samplemeanlist.append(sample.mean())

acollec = pd.DataFrame()
acollec['meanlist'] = samplemeanlist
acollec.hist(bins=100, density=1,figsize=(15,8))