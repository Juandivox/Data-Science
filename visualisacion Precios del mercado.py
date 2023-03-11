#visualisacion Precios del mercado

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# In[1] importar datos
#vamos a leer e importar el archivo CSV de sp500
spx = pd.read_csv('C:/Users/Usuario/Desktop/Bases de datos/US500_H1.csv') #no olvidar colocar la extencion csv
#en este caso la base de datos esta limpia osea no toca modificar
# In[2] comprobacion que tenemos los datos
#confirmamos que tenemos los datos
spx.head() #para ver los primeros datos
#spx.tail() #para ver la cola
spx.info() #informacion

# In[3] Graficacion completa
#para graficar todo se coloca lo siguiente
plt.plot(spx['DATE'], spx['CLOSE'])
plt.grid(True) #añade las mallas en el grafico
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("S&P 500 Closing Prices")
plt.show() #muestra el grafico

# In[4] convercion de fechas
# convertir la columna "fecha" a un objeto de fecha y hora de Pandas
spx['DATE'] = pd.to_datetime(spx['DATE'], infer_datetime_format=True)
spx['DATE'] = spx['DATE'].dt.strftime('%y-%m-%d')
spx['DATE'] = pd.to_datetime(spx['DATE'], format='%y-%m-%d')

print(spx['DATE']) #comprobar que todo se hizo de forma correcta
spx.head()


# In[5] Graficacion de un periodo espesifico !error extraño¡

spxenero3 = spx.loc["03-01-2023":'30-01-2023', 'DATE':'CLOSE'] #el error es que no deja colocarlo en la forma default aunque funciona con otro formato de fecha
plt.figure(figsize=(10, 8))
spxenero3['CLOSE'].plot()
plt.show()

