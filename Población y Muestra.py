#In[0]
import pandas as pd
import numpy as np


#In[1]Crear un marco de datos de población con 10 datos
data = pd.DataFrame()
data['Population'] = [47, 48, 85, 20, 19, 13, 72, 16, 50, 60]

#In[2]Extraiga una muestra con reemplazo, tamaño = 5 de la población
a_sample_with_replacement = data['Population'].sample(5, replace=True)
print(a_sample_with_replacement)

#In[3]Extraiga una muestra sin reemplazo, tamaño = 5 de la población
a_sample_without_replacement = data['Population'].sample(5, replace=False)
print(a_sample_without_replacement)

#In[4]Calcular media y varianza
population_mean = data['Population'].mean()
population_var = data['Population'].var(ddof=0)
print('Population mean is ', population_mean)
print('Population variance is', population_var)

#In[5] Calcule la media de la muestra y la desviación estándar de la muestra, tamaño = 10
# Obtendrá una media y una variación diferentes cada vez que ejecute el siguiente código
a_sample = data['Population'].sample(10, replace=True)
sample_mean = a_sample.mean()
sample_var = a_sample.var()
print('Sample mean is ', sample_mean)
print('Sample variance is', sample_var)

#In[6]Promedio de un estimador insesgado
sample_length = 500
sample_variance_collection=[data['Population'].sample(10, replace=True).var(ddof=1) for i in range(sample_length)]