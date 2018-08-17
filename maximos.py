#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 14:55:02 2017

@author: ezequiel
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelmax

#==============================================================================
# importo el archivo de datos con tiempos y voltajes V(t)
#==============================================================================
# poner el archivo txt en la misma carpeta que este archivo!
data = pd.read_csv('text.txt', header = 2,delimiter = '\t', decimal = '.')

#poner los nombres que correspondan a las columnas del archivo que queremos leer
t=data.time
F=data.V


#==============================================================================
# Buscar los maximos locales
#==============================================================================
radius=5 #cantidad de puntos a izquierda y derecha a comparar para determinar si un punto es maximo

max_positions=argrelmax(np.array(F),order=radius) #max_positions es un array con las poisiciones de los maximos locales   
                     
# ahora con esas posiciones de los maximos calculo las coordenadas (x,y) de cada uno                       

maximos=[]
t_maximos=[]

for i in range(len(max_positions[0])):
    j = max_positions[0][i]
    maximos.append(list(F)[j])
    t_maximos.append(list(t)[j])

#==============================================================================
# figura 1. Fuerza en funcion del tiempo con los maximos encontrados
#==============================================================================
fig0 = plt.figure(1)   
plt.cla()
F_t = fig0.add_subplot(111)
F_t.plot(t,F)
F_t.set_xlabel('Tiempo [unidades de t]')
F_t.set_ylabel('Fuerza [unidades de F]')

# grafico los maximos que calule
F_t.scatter(t_maximos,maximos,color='red')

fsave='grafico1.pdf' # guarda este archivo en la misma carpeta
plt.savefig(fsave,format='pdf') # guardar el grafico, en formato pdf


#==============================================================================
# guardo todo en un archivo de excel usando pandas
#==============================================================================
Maximos = pd.DataFrame({'Fuerza': maximos, 'Tiempo': t_maximos})

writer = pd.ExcelWriter('datos.xlsx', engine='xlsxwriter')

Maximos.to_excel(writer, sheet_name='Hoja1')

writer.save()