#!/usr/bin/env python3

import numpy as np, scipy as sp, scipy.fftpack as fft
import matplotlib.pyplot as plt

Fs = 1000  # Taxa de amostragem (Hz)
Ts = 1/Fs  # Tempo entre amostras = 1/Fs

t = np.arange(0, 2*np.pi, Ts)  # Vetor tempo

F1 = 10    # Frequencias do sinal composto
F2 = 50
F3 = 100

# Construir a forma de onda composta
y = np.sin(2*np.pi*F1*t) + np.sin(2*np.pi*F2*t) + np.sin(2*np.pi*F3*t)

# Fazer o FFT
Y = np.abs(fft.fft(y))
Y = Y[0:len(Y)/2] # E pegar so os elementos pares
f = np.arange(0, len(Y)) * Fs/len(y)    # Calcular o vetor frequencia

# Fazer os graficos
plt.subplot(211)
plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.xlim([0, 2*np.pi])
plt.ylabel('Amplitude (V)')

plt.subplot(212)
plt.plot(f, Y)
plt.xlabel('f(Hz)')
plt.ylabel('Y')
plt.xticks(np.arange(0, Fs, 50))
plt.show()
