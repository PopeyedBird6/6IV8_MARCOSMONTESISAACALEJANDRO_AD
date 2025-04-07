#Calcularemos las distancias entre todos los pares de puntos y determinaremos cuales estan mas alejados entre si y cuales estan mas cercanos utilizando las distancias Euclidiana, Manhattan y Chebyshev.
import numpy as np
import pandas as pd
from scipy.spatial import distance

puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1),
}
#Convertir las coordenadas a un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print(df_puntos)

def calcular_distancia(puntos):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j: #No calcular la distancia entre el mismo punto
                distancias.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
    return distancias
distancias = calcular_distancia(puntos)
valormax = distancias.values.max()
(punto1, punto2) = distancias.stack().idxmax()
valormin = distancias.values.min()
print("\nTabla de distancias:")
print(distancias)
print("\nDistancia máxima", valormax)
print("Entre los puntos", punto1, "y", punto2)

#Otra manera
max_value = distancias.max().max()
#obtener la columna que contiene el valor maximo
col_max = distancias.max().idxmax()

#obetner el indice que contiene el maximo 
id_max = distancias[col_max].idxmax()
print(f"valor maximo: {max_value} entre {col_max} y {id_max}")


##Distancia Manhattan
def calcular_distancia_manhattan(puntos):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j: 
                distancias.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
    return distancias
distancias_manhattan = calcular_distancia_manhattan(puntos)
valormax_manhattan = distancias_manhattan.values.max()
(punto1_manhattan, punto2_manhattan) = distancias_manhattan.stack().idxmax()
valormin_manhattan = distancias_manhattan.values.min()
print("\nTabla de distancias Manhattan:")
print(distancias_manhattan)
print("\nDistancia máxima", valormax_manhattan)
print("Entre los puntos", punto1_manhattan, "y", punto2_manhattan)

max_value_manhattan = distancias_manhattan.max().max()

col_max_manhattan = distancias_manhattan.max().idxmax()
id_max_manhattan = distancias_manhattan[col_max_manhattan].idxmax()
print(f"valor maximo: {max_value_manhattan} entre {col_max_manhattan} y {id_max_manhattan}")


##Distancia Chebyshev
def calcular_distancia_chebyshev(puntos):
    distancias = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
    for i in df_puntos.index:
        for j in df_puntos.index:
            if i != j: 
                distancias.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])
    return distancias
distancias_chebyshev = calcular_distancia_chebyshev(puntos)
valormax_chebyshev = distancias_chebyshev.values.max()
(punto1_chebyshev, punto2_chebyshev) = distancias_chebyshev.stack().idxmax()
valormin_chebyshev = distancias_chebyshev.values.min()
print("\nTabla de distancias Chebyshev:")
print(distancias_chebyshev)
print("\nDistancia máxima", valormax_chebyshev)
print("Entre los puntos", punto1_chebyshev, "y", punto2_chebyshev)

max_value_chebyshev = distancias_chebyshev.max().max()
col_max_chebyshev = distancias_chebyshev.max().idxmax()

id_max_chebyshev = distancias_chebyshev[col_max_chebyshev].idxmax()
print(f"valor maximo: {max_value_chebyshev} entre {col_max_chebyshev} y {id_max_chebyshev}")