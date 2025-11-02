# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 15:23:25 2025

@author: Augusto
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


#Coeficientes
ba=[1,1,1,1]
bb=[1,1,1,1,1]
bc=[1,-1]
bd=[1,-1]

#cte 
fs=1000 #Hz

#freqz para cada caso
wa,ha=sig.freqz(b=ba,whole=False,fs=fs) #a=1 como para nuestro caso y whole=false para ir de [0 a pi] asi tengo radianes/muestras
wb,hb=sig.freqz(b=bb,a=1,whole=False, fs=fs)
wc,hc=sig.freqz(b=bc,a=1,whole=False, fs=fs)
wd,hd=sig.freqz(b=bd,a=1,whole=False, fs=fs)

#maginitud y fase
maga=np.abs(ha) #Modulo T(e^jΩ)
fasea=np.unwrap(np.angle(ha)) #Fase T(e^jΩ) (radianes)
magb=np.abs(hb) #Modulo T(e^jΩ)
faseb=np.unwrap(np.angle(hb)) #Fase T(e^jΩ) (radianes) 
magc=np.abs(hc) #Modulo T(e^jΩ)
fasec=np.unwrap(np.angle(hc)) #Fase T(e^jΩ) (radianes)
magd=np.abs(hd) #Modulo T(e^jΩ)
fased=np.unwrap(np.angle(hd)) #Fase T(e^jΩ) (radianes)


#graficos
plt.figure()
plt.plot(wa, maga)
plt.title('Respuesta en frecuencia |t(e^{jΩ})|')
plt.ylabel('Modulo |t(e^{jΩ})|')
plt.xlabel('frecuencia (Hz)')

plt.figure()
plt.plot(wa, fasea)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')

plt.figure()
plt.plot(wb, magb)
plt.title('Respuesta en frecuencia |t(e^{jΩ})|')
plt.ylabel('Modulo |t(e^{jΩ})|')
plt.xlabel('frecuencia (Hz)')

plt.figure()
plt.plot(wb, faseb)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')

plt.figure()
plt.plot(wc, magc)
plt.title('Respuesta en frecuencia |t(e^{jΩ})|')
plt.ylabel('Modulo |t(e^{jΩ})|')
plt.xlabel('frecuencia (Hz)')

plt.figure()
plt.plot(wc, fasec)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')

plt.figure()
plt.plot(wd, magd)
plt.title('Respuesta en frecuencia |t(e^{jΩ})|')
plt.ylabel('Modulo |t(e^{jΩ})|')
plt.xlabel('frecuencia (Hz)')

plt.figure()
plt.plot(wd, fased)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Fase [rad]')



