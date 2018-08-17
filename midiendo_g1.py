# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#==============================================================================
# importo el archivo de datos con tiempos y voltajes V(t)
#==============================================================================

data = pd.read_csv('text.txt', header = 2,delimiter = '\t', decimal=',')

t=data.time
V=data.V



#==============================================================================
# figura 0. Voltaje en funcion del tiempo
#==============================================================================
fig0 = plt.figure(0)   
plt.cla()
vo_t = fig0.add_subplot(111)
vo_t.plot(t,V,color='blue')
vo_t.scatter(t,V,color='blue')
vo_t.set_xlabel('Tiempo [unidades de t]')
vo_t.set_ylabel('Voltaje [unidades de V]')


#==============================================================================
# calculo como cambia la posicion respecto del tiempo
#==============================================================================

umbral=2.8 #  0.28 
d=1.0 #distancia entre lineas negras

T=[]
X=[]
for i in range(len(t)-1):
    if V[i]>umbral and V[i+1]<=umbral: #pedimos que V(t) decrezca
        T.append((t[i]+t[i+1])/2.)
        X.append(len(T)*d)
        
      
#==============================================================================
# figura 1. Posicion en funcion del tiempo
#==============================================================================
fig1 = plt.figure(1)       
plt.cla()
x_t = fig1.add_subplot(111)
x_t.plot(T,X,color='blue')
x_t.scatter(T,X,color='blue')
x_t.set_xlabel('Tiempo [unidades de t]')
x_t.set_ylabel(u'Posición [unidades de x]')

#Dibujo el umbral y los puntos marcados con nuestro crierio
vo_t.plot(t,umbral*np.ones(len(t)),color='gray')        
vo_t.scatter(T,umbral*np.ones(len(T)),color='red') 
vo_t.text(max(T)+.1,umbral,'Umbral')

#==============================================================================
# calculo la velocidad en funcion del tiempo
#==============================================================================

#para graficar necesito un T del mismo largo que V
V=[]#velocidad
T2=[]#tiempo
for i in range(len(X)-1):
    Tpromedio=(T[i+1]+T[i])/2.0
    deltaT=T[i+1]-T[i]   
    deltaX=X[i+1]-X[i]   
    V.append(deltaX/deltaT)
    T2.append(Tpromedio)
    
#==============================================================================
# figura 2. Velocidad en funcion del tiempo
#==============================================================================
fig2 = plt.figure(2)   
plt.cla()
v_t = fig2.add_subplot(111)
v_t.plot(T2,V, color='orange')
v_t.scatter(T2,V, color='orange')
v_t.set_xlabel('Tiempo [unidades de t]')
v_t.set_ylabel('Velocidad [unidades de v]')

#==============================================================================
# guardo todo en un archivo de excel usando pandas
#==============================================================================
dfX = pd.DataFrame({'Tiempo': T,'Posicion': X})
dfV = pd.DataFrame({'Tiempo': T2,'Velocidad': V})

writer = pd.ExcelWriter('datos.xlsx', engine='xlsxwriter')

dfX.to_excel(writer, sheet_name='Hoja_X')
dfV.to_excel(writer, sheet_name='Hoja_Vel')

writer.save()
