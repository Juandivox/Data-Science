#In[0]Importacion de librerias
import numpy as np
import pandas as pd

#In[1]Imita el juego de dados
# tirar dos dados varias veces
dado = pd.DataFrame([1, 2, 3, 4, 5, 6])
suma_de_dado = dado.sample(2, replace=True).sum().loc[0]
print('la suma de los dados es ', suma_de_dado) 
#puede obtener diferentes resultados ya que ahora imitamos el resultado de lanzar 2 dados, pero el rango debe limitarse entre 2 y 12.

#In[2]¡Es tu turno! reemplacemos el ninguno con el código de tirar tres dados, en lugar de dos
np.random.seed(1)  # This is for checking answer, do NOT modify this line of code
sum_of_three_dice = dado.sample(3, replace=True).sum().loc[0]
print('Sum of three dice is', sum_of_three_dice)

#In[3]Imita el juego de dados de rollo varias veces.
# El siguiente código imita el juego de tirar los dados 50 veces. Y todos los resultados se almacenan en "Resultado"
# Probemos y obtengamos los resultados de 50 suma de caras.

trial = 50
result = [dado.sample(2, replace=True).sum().loc[0] for i in range(trial)]
print(result[:10])
