# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

#==============================================================================
# IMPORTACIÓN DE LAS BIBLIOTECAS QUE NECESITAMOS USAR
#==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#==============================================================================
# IMPORTACIÓN DE LOS DATOS DESDE UN ARCHIVO DE EXCEL
#==============================================================================

#uso la biblioteca 'pandas'

xls_file = pd.ExcelFile('C:/Users/Win7 32 virtual/Desktop/data.xls') # Importar el archivo de Excel de esta dirección

df = xls_file.parse('Hoja1') # En particular los datos de esta hoja

data = np.array(df) # Guardo en la variable data los datos que importé, en forma de array (es como una matriz)

x = data[:,0] # guardo en la variable x todos los datos de la columna 0

# tener en cuenta que en python las cosas se numeran desde el cero, no desde el 1.

#==============================================================================
# GRAFICAR EL HISTOGRAMA DE LOS DATOS
#==============================================================================

# uso la biblioteca matplotlib.pyplot

plt.close('all') # amtes de graficar, cierro todos las figuras que estén abiertas

bins=10 # número de bins del histograma

n,bin_positions,p = plt.hist(x,bins,normed=False,label='datos 1') # grafico el histograma
#esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p

#le pongo nombres a los ejes
plt.xlabel(r'Tiempo de caída (s)')
plt.ylabel('Cuentas')

#==============================================================================
# CALCULAR LA MEDIA, LA DESVIACIÓN ESTÁNDAR DE LOS DATOS y EL NÚMERO TOTAL DE CUENTAS
#==============================================================================

# uso la biblioteca numpy

mu=np.mean(x) # media

sigma=np.std(x) #desviación estándar

N=len(x) # número de cuentas

std_err = sigma / N # error estándar

# muestro estos resultados

print( 'media: ', mu)
print( 'desviacion estandar: ', sigma)
print( 'total de cuentas: ', N)
print( 'error estandar: ', std_err)

#==============================================================================
# CALCULAR LA GAUSSIANA QUE MEJOR AJUSTA Y GRAFICARLA
#==============================================================================

bin_size=bin_positions[1]-bin_positions[0] # calculo el ancho de los bins del histograma

x_gaussiana=np.linspace(mu-5*sigma,mu+5*sigma,num=100) # armo una lista de puntos donde quiero graficar la distribución de ajuste

gaussiana=mlab.normpdf(x_gaussiana, mu, sigma)*N*bin_size # calculo la gaussiana que corresponde al histograma

plt.plot(x_gaussiana,gaussiana,'r--', linewidth=2, label='ajuste 1') #grafico la gaussiana

#==============================================================================
# GUARDAR EL GRÁFICO
#==============================================================================

fsave='C:/Users/Win7 32 virtual/Desktop/hist.pdf' # dirección donde lo quiero guardar

plt.savefig(fsave,format='pdf') # guardar el grafico, en formato pdf

