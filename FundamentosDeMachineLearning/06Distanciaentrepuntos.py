import numpy as np
import pandas as pd
from scipy.spatial import distance
#Definimos la coordenadas de las tiendas
tiendas = {
    'Tienda A': (1, 1),
    'Tienda B': (1, 5),
    'Tienda C': (7, 1),
    'Tienda D': (3, 3),
    'Tienda E': (4, 8),
}
#Convertir las coordenadas a un DataFrame
df_tiendas = pd.DataFrame(tiendas).T
df_tiendas.columns = ['X', 'Y']
print(df_tiendas)

# Inicializamos un DataFrame para almacenar las distancias
distancia_eu = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancia_mh = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancia_ch = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

# Calculos de las distancias
for i in df_tiendas.index:
    for j in df_tiendas.index:
        # Distancia euclidiana
        distancia_eu.loc[i, j] = distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        # Distancia Manhattan
        distancia_mh.loc[i, j] = distance.cityblock(df_tiendas.loc[i], df_tiendas.loc[j])
        # Distancia Chebyshev
        distancia_ch.loc[i, j] = distance.chebyshev(df_tiendas.loc[i], df_tiendas.loc[j])
#Mostrar los resultados
print("\nDistancia Euclidiana:")
print(distancia_eu)
print("\nDistancia Manhattan:")
print(distancia_mh)
print("\nDistancia Chebyshev:")
print(distancia_ch)