#In[0]Importacion librerias
import pandas as pd
import matplotlib.pyplot as plt

#In[1] importacion datos
#Importar la información de la vivienda para su análisis
viviendas = pd.read_csv("C:/Users/Usuario/Desktop/Bases de datos/housing.csv")
viviendas.head()

#In[2]Asociación entre dos variables aleatorias
## Usa la covarianza para calcular la asociación
viviendas.cov()

#In[3] Usar correlación para calcular la asociación es más apropiado en este caso
viviendas.corr()

#In[4]# diagrama de matriz de dispersión
from pandas.plotting import scatter_matrix
sm = scatter_matrix(viviendas, figsize=(10, 10))

#In[5]¡Hagamos un análisis por ti mismo!
#Observe la asociación entre LSTAT y MEDV:
# Esta vez echamos un vistazo más de cerca a MEDV vs LSTAT.
#¿Cuál es la asociación que observó entre MEDV y LSTAT?
viviendas.plot(kind='scatter', x='LSTAT', y='MEDV', figsize=(10, 10))