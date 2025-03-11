import pandas as pd

def resumen(fichero):
    df = pd.read_csv(fichero, sep=';', decimal='.', thousands=',', index_col=0)
    df = df.apply(pd.to_numeric, errors='coerce')
    return pd.DataFrame([df.min(), df.max(), df.mean(), df.std()], index=['Min', 'Max', 'Media', 'Desviacion'])

print(resumen('ElementosBasicosEstadistica/cotizacion.csv'))
