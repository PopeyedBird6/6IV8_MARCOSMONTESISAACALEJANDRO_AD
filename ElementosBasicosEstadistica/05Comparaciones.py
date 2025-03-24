import numpy as np
import matplotlib.pyplot as plt

#Crear una semilla random para reproducibilidad
np.random.seed(0)

#Buscar los parametros para una distribucion 
#media
media = 0
#Desviacion estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#El numero de muestras para el analisis
n_muestras = 1000

#Generar los datos de la distribucion
datos1 = np.random.normal(media, sigma1, n_muestras)
datos2 = np.random.normal(media, sigma2, n_muestras)
datos3 = np.random.normal(media, sigma3, n_muestras)

#Crear la grafica
plt.figure(figsize=(10,6))

#Cargar las frecuencias a partir de una grafica de histograma
plt.hist(datos1, bins=30, color='blue', density='True', label='Desviación Estandar = 1', alpha=0.5)
plt.hist(datos2, bins=30, color='red', density='True', label='Desviación Estandar = 2', alpha=0.5)
plt.hist(datos3, bins=30, color='green', density='True', label='Desviación Estandar = 3', alpha=0.5)

#Graficar
plt.title('Comparacion de Distribuciones Normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

#Mostrar la grafica
plt.show()