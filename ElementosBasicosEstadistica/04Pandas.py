import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# Mostrar las primeras cinco filas
print(df.head())

# Mostrar las últimas cinco filas
print(df.tail())

# Mostrar una fila en específico
print(df.loc[7])

# Mostrar la columna ocean_proximity
print(df['ocean_proximity'])

# Obtener la media de la columna total_rooms
print(df['total_rooms'].mean())

# Obtener la mediana de la columna total_bedrooms
print(df['total_bedrooms'].median())

# Obtener la suma de la columna population
print(df['population'].sum())

# Filtrar por ocean_proximity == 'ISLAND'
print(df[df['ocean_proximity'] == 'ISLAND'])
