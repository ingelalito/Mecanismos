#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 11:45:33 2022

@author: eduardocontreras
"""
import matplotlib . pyplot as plt
import numpy as np
print("Velocidad de rotación de parejas de engranajes")
print("El cálculo de la velocidad  de rotación se determina por: ")
print("Nm *Zm= Ns *Zs  ")
print("\nZm = dientes de engranaje motor"+
               "\nNm = velocidad de rotación del engranaje motor rpm"+
               "\nZs = dientes de engranaje salida"+
               "\nNm = velocidad de rotación del engranaje salida rpm")
print("Cálculo de la velocidad de rotación de salida Ns en rpm  ")
print("Ns = Nm *Zm/ Zs  ")
print("Proporcione los valores de los datos")
Zm =int(input("dientes de engranaje motor: "))
Nm =int(input(" velocidad de rotación del engranaje motor rpm: "))
print("Cálculo de Ns en función de  Zs  ")
print(" Zs varía en el rango de 10 a 120 dientes ")
# 100 linearly spaced numbers
Zs = np.linspace(10,120,100)
# the function, which is y = x3 here
Ns= Nm *Zm/ Zs


plt.plot(Zs, Ns, 'r', label='Ns = Nm *Zm/ Zs')
plt.title ( 'Graph of Ns = Nm *Zm/ Zs ')
plt.xlabel('Xs', color='#1C2833') 
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid ()
plt.show()

