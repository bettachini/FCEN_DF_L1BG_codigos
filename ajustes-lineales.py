# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 16:50:29 2015
@author: Dieg Shalom, Fabricio  Della Picca y Ezequiel Galpern
        Labo F1ByG Cátedra Estrada, 1C 2017
"""

#==============================================================================
# IMPORTACIÓN DE LAS BIBLIOTECAS QUE NECESITAMOS USAR
#==============================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.mlab as mlab
from scipy.optimize import curve_fit
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

#==============================================================================
# IMPORTACIÓN DE LOS DATOS DESDE UN ARCHIVO DE EXCEL
#==============================================================================

directorio = 'D:/micarpeta/'
nombrearchivo='miarchivo.xls'

xls_file = pd.ExcelFile(directorio + nombrearchivo) # Importar el archivo de Excel de esta dirección

df = xls_file.parse('data') # En particular los datos de esta hoja

data = np.array(df) # Guardo en la variable data los datos que importé, en forma de array (es como una matriz)

x = data[:,0] # guardo en la variable x todos los datos de la columna 0

y = data[:,1] # guardo en la variable y todos los datos de la columna 1

yerr = data[:,2] # guardo en la variable yerr todos los datos de la columna 2
                   
#==============================================================================
# Ajustes lineales
#==============================================================================

f = lambda x, B, M: M * x + B # la función modelo, con la que ajustamos

print('Ajuste lineal')
popt, pcov = curve_fit(f, x, y)#ajusto sin incertezas en y
sigmas = np.sqrt([pcov[0,0],pcov[1,1]])# las incertezas de los parametros son la raiz de la diagonal de la matriz de covarianza
b=popt[0]
m=popt[1]
eb=sigmas[0]
em=sigmas[1]
print('Ordenada al origen: ' + str(b) + ' ± ' + str(eb))
print('Pendiente ' + str(m) + ' ± ' + str(em))

print('Ajuste lineal con incertezas en y')
popt, pcov = curve_fit(f, x, y, sigma = yerr,absolute_sigma=True)#ajusto con incertezas en y
                #sigma son las incertezas en y. absolute_sigma para que las considere absolutas.
sigmas = np.sqrt([pcov[0,0],pcov[1,1]])# las incertezas de los parametros son la raiz de la diagonal de la matriz de covarianza
b=popt[0]
m=popt[1]
eb=sigmas[0]
em=sigmas[1]
print('Ordenada al origen: ' + str(b) + ' ± ' + str(eb))
print('Pendiente ' + str(m) + ' ± ' + str(em))

#==============================================================================
# graficamos
#==============================================================================
plt.errorbar(x,y,yerr=yerr,color='b')#,10000,fmt='-o',color='g')
plt.plot(x,y,'-ob')#,10000,fmt='-o',color='g')
plt.plot(x,m*x+b,'r')#,10000,fmt='-o',color='g')
plt.xlabel('x [unidades de x]')
plt.ylabel('y [unidades de y]')
plt.title('Ajuste con incertezas en y')
plt.legend(("Datos","Ajuste"), loc=4)
plt.grid('on')#para que muestre la grilla
