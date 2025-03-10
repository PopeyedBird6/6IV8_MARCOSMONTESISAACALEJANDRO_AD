import pandas as pd

##Escribir una funcion que recib aun diccionario con las ontas de los estudiantes del curso y devuelve una serie con minimo, maximo, media, desviacion estandar

def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std()], index =['Minimo', 'Maximo', 'Desviacion estandar'])
    return estadisticas

notas = {'Juan': 10, 'Isaac': 1, 'Fabian': 6, 'Maxi': 2, 'Owen': 3, 'Maria': 4, 'Maclovio': 1}

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas>= 5].sort_values(ascending=false)

print(estadistica_notas(notas))