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

xls_file = pd.ExcelFile('E:/datos.xlsx') # Importar el archivo de Excel de esta dirección

df = xls_file.parse('Sheet1') # En particular los datos de esta hoja

data = np.array(df) # Guardo en la variable data los datos que importé, en forma de array (es como una matriz)

x = data[:,0] # guardo en la variable x todos los datos de la columna 0

# tener en cuenta que en python las cosas se numeran desde el cero, no desde el 1.

y = data[:,1] # guardo en la variable x todos los datos de la columna 1

#==============================================================================
# GRAFICAR EL HISTOGRAMA DE LOS DATOS
#==============================================================================

# uso la biblioteca matplotlib.pyplot

plt.close('all') # amtes de graficar, cierro todos las figuras que estén abiertas

bins=10 # número de bins del histograma

n,bin_positions,p = plt.hist(x,bins,normed=False,label='datos 1') # grafico el histograma
#esta funcion, ademas de graficar devuelve parametros del histograma, que guardamos en las variables n,bin_positions,p

n2,bin_positions2,p2 = plt.hist(y,bins,normed=False, label='datos 2') # grafico el histograma 2

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

print( 'media 1: ', mu)
print( 'desviacion estandar 1: ', sigma)
print( 'total de cuentas 1: ', N)
print( 'error estandar 1: ', std_err)

mu2=np.mean(y) # media

sigma2=np.std(y) #desviación estándar

N2=len(y) # número de cuentas

std_err2 = sigma2 / N2

# muestro estos resultados

print( 'media 2: ', mu2)
print( 'desviacion estandar 2: ', sigma2)
print( 'total de cuentas 2: ', N2)
print( 'error estandar 2: ', std_err2)

#==============================================================================
# CALCULAR LA GAUSSIANA QUE MEJOR AJUSTA Y GRAFICARLA
#==============================================================================

bin_size=bin_positions[1]-bin_positions[0] # calculo el ancho de los bins del histograma

x_gaussiana=np.linspace(mu-5*sigma,mu+5*sigma,num=100) # armo una lista de puntos donde quiero graficar la distribución de ajuste

gaussiana=mlab.normpdf(x_gaussiana, mu, sigma)*N*bin_size # calculo la gaussiana que corresponde al histograma

plt.plot(x_gaussiana,gaussiana,'r--', linewidth=2, label='ajuste 1') #grafico la gaussiana


bin_size2=bin_positions2[1]-bin_positions2[0] # calculo el ancho de los bins del histogra

y_gaussiana=np.linspace(mu2-5*sigma2,mu2+5*sigma2,num=100) # armo una lista de puntos donde quiero graficar la distribución de ajuste

gaussiana2=mlab.normpdf(y_gaussiana, mu2, sigma2)*N2*bin_size2 # calculo la gaussiana que corresponde al histograma

plt.plot(y_gaussiana,gaussiana2,'r--', linewidth=2, label='ajuste 1') #grafico la gaussiana

#==============================================================================
# GUARDAR EL GRÁFICO
#==============================================================================

fsave='E:/borrar/hist2.pdf' # dirección donde lo quiero guardar

plt.savefig(fsave,format='pdf') # guardar el grafico, en formato pdf

