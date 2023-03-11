#In[0]importacion librerias
import pandas as pd
import matplotlib.pyplot as plt

#In[1] Para recordar, este es el código para imitar el juego de dados 50 veces
die = pd.DataFrame([1, 2, 3, 4, 5, 6])
trial = 50
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]

#In[2] Este es el código para resumir los resultados de la suma de caras por frecuencia
freq = pd.DataFrame(results)[0].value_counts()
"""value_counts() cuenta la frecuencia de cada valor único en esta columna 
y devuelve un nuevo objeto DataFrame con los valores únicos en el índice y su frecuencia en la columna.
"sort_freq" que ordena los valores únicos en el índice del objeto "freq" de forma ascendente, 
utilizando el método sort_index(). Esto se hace para que los resultados aparezcan en orden numérico."""
sort_freq = freq.sort_index()
print(sort_freq)

#In[3]trazar la base del gráfico de barras en el resultado
sort_freq.plot(kind='bar', color='blue', figsize=(15, 8))

#In[4] Frecuencia relativa
"""Usando la frecuencia relativa, podemos cambiar la escala de la frecuencia 
para que podamos comparar los resultados de diferentes números de ensayos"""
relative_freq = sort_freq/trial
relative_freq.plot(kind='bar', color='blue', figsize=(15, 8))

#In[5]Intentemos aumentar el número de intentos a 10000 y veamos qué sucede...
trial = 10000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]
freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()
relative_freq = sort_freq/trial
relative_freq.plot(kind='bar', color='blue', figsize=(15, 8))
"""Podemos ver que con más intentos, el resultado parece más y más estable, 
y esto está muy cerca de una distribución de probabilidad. 
Intente aumentar aún más el número de pruebas"""
#In[6]Expectativa y Varianza de una distribución
# supongamos que tenemos dados justos, lo que significa que todas las caras se mostrarán con la misma probabilidad
# entonces podemos decir que conocemos la 'Distribución' de la variable aleatoria - sum_of_dice

X_distri = pd.DataFrame(index=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
X_distri['Prob'] = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
X_distri['Prob'] = X_distri['Prob']/36
print(X_distri)

mean = pd.Series(X_distri.index * X_distri['Prob']).sum()
var = pd.Series(((X_distri.index - mean)**2)*X_distri['Prob']).sum()
#Produce la media y la varianza de la distribución. La media y la varianza se pueden usar para describir una distribución
print(mean, var)

#In[7]Media empírica y varianza
#si calculamos la media y la varianza de los resultados 
# (con un número suficientemente alto de ensayos, por ejemplo, 20000)...
trial = 20000
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]

#imprime la media y la varianza de los 20000 ensayos
results = pd.Series(results)
print(results.mean(), results.var())
