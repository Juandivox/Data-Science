#In[0]Confidence Interval #importacion de librerias
import pandas as pd
import numpy as np
from scipy.stats import norm

#In[1] importacion de datos

spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_Daily.csv')
spx.head()

#In[2] Estime el rendimiento medio de las acciones con un intervalo de confianza del 90 %
# usaremos el retorno de logaritmico para el retorno promedio de acciones de Microsoft

spx['logReturn'] = np.log(spx['CLOSE'].shift(-1)) - np.log(spx['CLOSE'])

#In[3]Construyamos un intervalo de confianza del 95 % para la devolución del logaritmo

sample_size = spx['logReturn'].shape[0]
sample_mean = spx['logReturn'].mean()
sample_std = spx['logReturn'].std(ddof=1) / sample_size**0.5 #error estandar

#Nesesitamos saber cual es la confianza en este caso 95%
confianza_base= 95 #esta no se puede usar por eso se divide en dos
confianza = confianza_base/100 #con esta podemos calcular alpha
print('la confianza es ',confianza)

#una vez con este dato podemos sacar alpha y alpha/2
alpha=1-confianza
print('alpha es ',alpha)
alphaq= alpha/2
print('alpha/2 es ',alphaq)
#y para calcular z se usa
z=norm.ppf(confianza)
print('z es ',z)

#quartiles
q25= alphaq
q75= 1-alphaq

# cuantil izquierdo y derecho
z_left_25 = norm.ppf(q25) 
z_right_75 = norm.ppf(q75)

# límite superior e inferior
interval_left = sample_mean - z_right_75 * (sample_std)
interval_right = sample_mean - z_left_25 * (sample_std)

print('Intervalo de confianza al 95%:', (interval_left, interval_right))
#In[4]El intervalo de confianza del 90% le dice que habrá un 90% de posibilidades de 
# que el rendimiento promedio de las acciones se encuentre entre "interval_left"
# e "intervalo_derecho".

print('90% confidence interval is ', (interval_left, interval_right))
