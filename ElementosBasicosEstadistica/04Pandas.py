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

# Filtrar
print(df[df['ocean_proximity'] == 'ISLAND'])

# Crear una gráfica de dispersión entre total_rooms y median_house_value
plt.figure(figsize=(8, 6))
plt.scatter(df['total_rooms'], df['median_house_value'], alpha=0.3, color='blue')

# Agregar títulos y etiquetas
plt.title('Relación entre Total de Habitaciones y Valor Medio de la Casa')
plt.xlabel('Total de Habitaciones')
plt.ylabel('Valor Medio de la Casa')

# Mostrar la gráfica
plt.show()
