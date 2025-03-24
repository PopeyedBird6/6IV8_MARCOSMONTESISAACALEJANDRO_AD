import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

catalogo_sucursal = pd.read_excel('ElementosBasicosEstadistica/Catalogo_sucursal.xlsx')
proyecto1 = pd.read_excel('ElementosBasicosEstadistica/proyecto1.xlsx')

#Ventas totales del comercio
vtotales = proyecto1['ventas_tot'].sum()
print(f'Las ventas totales del comercio son: {vtotales}')

#Clientes con adeudos
adeudo = proyecto1[proyecto1['adeudo_actual'] > 0].shape[0]
print(f'Hay {adeudo} clientes con adeudos')
#Clientes sin adeudos
sin_adeudo = proyecto1[proyecto1['adeudo_actual'] == 0].shape[0]
print(f'Hay {sin_adeudo} clientes sin adeudos')
#Total de clientes
total_clientes = adeudo + sin_adeudo
#Porcentaje de clientes con adeudos
porcentaje_adeudo = (adeudo / total_clientes) * 100
print(f'El porcentaje de clientes con adeudos es: {porcentaje_adeudo:.2f}%')
#Porcentaje de clientes sin adeudos
porcentaje_sin_adeudo = (sin_adeudo / total_clientes) * 100
print(f'El porcentaje de clientes sin adeudos es: {porcentaje_sin_adeudo:.2f}%')

#Gráfica Ventas vs Tiempo
proyecto1['fec_ini_cdto'] = pd.to_datetime(proyecto1['fec_ini_cdto'])
ventas_por_fecha = proyecto1.groupby('fec_ini_cdto')['ventas_tot'].sum()
plt.figure(figsize=(10,6))
ventas_por_fecha.plot(kind='bar')
plt.title('Ventas vs Tiempo')
plt.xlabel('Fechas')
plt.ylabel('Ventas')
plt.show()

#Grafica Desviación Estandar vs Tiempo
