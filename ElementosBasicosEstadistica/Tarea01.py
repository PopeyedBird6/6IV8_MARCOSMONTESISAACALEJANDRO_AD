import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ElementosBasicosEstadistica/housing.csv')

# Estadisticas que pide el profe
columna = 'median_house_value'
estadisticas = {
    'Media': df[columna].mean(),
    'Mediana': df[columna].median(),
    'Moda': df[columna].mode()[0],
    'Rango': df[columna].max() - df[columna].min(),
    'Varianza': df[columna].var(),
    'Desviación Estándar': df[columna].std()
}

# Tabla de estadisticas
estadisticas_df = pd.DataFrame([estadisticas])
print(estadisticas_df)

# Tabla de frecuencias
tabla_frecuencias = df[columna].value_counts().sort_index().reset_index()
tabla_frecuencias.columns = [columna, 'Frecuencia']
print("\nTabla de Frecuencias:")
print(tabla_frecuencias)

# Crear graficas para cada variable porque no supe como hacerlo en todos 
variables = ['median_house_value', 'total_bedrooms', 'population']
titulos = ['Histograma de median_house_value', 'Histograma de total_bedrooms', 'Histograma de population']

for i, var in enumerate(variables):
    plt.figure(figsize=(6, 4))
    plt.hist(df[var].dropna(), bins=30, color=['blue', 'green', 'orange'][i], edgecolor='black')
    plt.title(titulos[i])
    plt.xlabel(var)
    plt.ylabel('Frecuencia')
    plt.show()
