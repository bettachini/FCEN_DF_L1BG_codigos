# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:55:55 2018

@author: Fede
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy

f=scipy.misc.imread('hoja_prueba.jpeg')
print(f.shape)
plt.imshow(f)
plt.show()


imag_hoja=f[170:1050,50:475,2] #[y,x,color]
imag_cuadrado = f[510:620,475:590,0]
plt.figure()
plt.imshow(imag_hoja)
plt.show()
plt.figure()
plt.imshow(imag_cuadrado)
plt.show()

print(0,0,imag_cuadrado[0,0])
print(40,40,imag_cuadrado[40,40])

imag_hoja = imag_hoja < 100
imag_cuadrado = imag_cuadrado  < 100

plt.imshow(imag_hoja)  
plt.show()
plt.imshow(imag_cuadrado)
plt.show()

cant_pixeles_hoja = sum(sum(imag_hoja))
cant_pixeles_cuadrado = sum(sum(imag_cuadrado))
cant_pixeles_cm = np.sqrt(cant_pixeles_cuadrado)

area_hoja = cant_pixeles_hoja / cant_pixeles_cuadrado

def extremos(imagen):
    n,m = imagen.shape
    arriba,abajo,izquierda,derecha =n,0,m,0
    for i in range(n):
        for j in range(m):
            if imagen[i,j]:
                if arriba > i:
                    arriba = i
                if abajo < i:
                    abajo = i
                if izquierda > j:
                    izquierda = j
                if derecha < j:
                    derecha = j
                
    return [arriba,abajo,izquierda,derecha]

[arriba,abajo,izquierda,derecha] = extremos(imag_hoja)
largo_hoja = (abajo-arriba)/cant_pixeles_cm
ancho_hoja = (derecha-izquierda)/cant_pixeles_cm






