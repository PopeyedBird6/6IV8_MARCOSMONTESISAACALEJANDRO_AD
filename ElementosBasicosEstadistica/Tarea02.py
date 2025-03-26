import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

catalogo_sucursal = pd.read_excel('ElementosBasicosEstadistica/Catalogo_sucursal.xlsx')
proyecto1 = pd.read_excel('ElementosBasicosEstadistica/proyecto1.xlsx')


##DATOS:


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

#Deuda total de los clientes
deuda_total = proyecto1['adeudo_actual'].sum()
print(f'La deuda total de los clientes es: {deuda_total}')
#Porcentaje de utilidad del comercio
utilidad = vtotales - deuda_total
porcentaje_utilidad = (utilidad / vtotales) * 100
print(f'El porcentaje de utilidad del comercio es: {porcentaje_utilidad:.2f}%')


##GRÁFICAS:


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
desviacion = proyecto1.groupby('fec_ini_cdto')['pagos_tot'].std()
plt.figure(figsize=(10,6))
desviacion.plot(kind='bar')
plt.title('Desviación Estándar de Pagos vs Tiempo')
plt.xlabel('Fechas')
plt.ylabel('Desviaciones')
plt.show()

#Gráfica circular de ventas por sucursal
#Hacer que el id y el nombre de la sucursal correspondan
proyecto1 = proyecto1.merge(catalogo_sucursal, left_on='id_sucursal', right_on='id_sucursal', how='left')
ventas_por_sucursal = proyecto1.groupby('suc')['ventas_tot'].sum()
plt.figure(figsize=(10,6))
ventas_por_sucursal.plot(kind='pie', autopct='%1.1f%%')
plt.title('Ventas por Sucursal')
plt.show()

#Gráfica deudas totales vs utilidad por cada sucursal
deudas_por_sucursal = proyecto1.groupby('suc')['adeudo_actual'].sum()
utilidad_por_sucursal = ventas_por_sucursal - deudas_por_sucursal
#Dataframe para combinar las deudas y utilidades
combinado = pd.DataFrame({
    'Deuda Total': deudas_por_sucursal,
    'Utilidad': utilidad_por_sucursal
})
combinado.plot(kind='bar', figsize=(10, 8), color=['red', 'green'], alpha=0.7)
plt.title('Deudas Totales vs Utilidad por Sucursal')
plt.xlabel('Sucursales')
plt.ylabel('Montos')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
