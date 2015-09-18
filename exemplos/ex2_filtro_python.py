#!/usr/bin/env python3

import numpy as np, scipy as sp, scipy.fftpack as fft
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, AutoLocator

Fs = 1000  # Taxa de amostragem (Hz)
Ts = 1/Fs  # Tempo entre amostras = 1/Fs

t = np.arange(0, 1, Ts)  # Vetor tempo

Forig = 60    # Frequencias do sinal composto
Fdirty1 = 120
Fdirty2 = 200


yorig = np.sin(2*np.pi*Forig*t)
y = yorig + 0.5*np.sin(2*np.pi*Fdirty1*t) + 0.8 * np.sin(2*np.pi*Fdirty2*t)

Y = np.abs(fft.fft(y))  # FFT do vetor Y
Y = Y[0:len(Y)/2]       # Pegar so' elementos pares
f = np.arange(0, len(Y)) * Fs/len(y)

## Fazer os graficos

fig = plt.figure(figsize=(12, 9))
ax = plt.axes()
# Sinal sujo no dominio do tempo
t_sujo = plt.subplot(2, 2, 1);
plt.plot(t, y)
plt.xlabel('Tempo(s)')
plt.xlim([0, t[-1]])
plt.ylabel('Amplitude (V)')
plt.title("Sinal sujo")

# FFT do sinal sujo
f_sujo = plt.subplot(2, 2, 3)
plt.plot(f, Y)
plt.xlabel('f (Hz)')
plt.ylabel('Y')

# Limpar o sinal
Wc = 75 / (Fs / 2)  # Corte = 75 Hz
[b, a] = signal.butter(6, Wc) # Filtro 6a ordem
yfilt = signal.filtfilt(b, a, y) # Aplicar filtro
Yfilt = np.abs(fft.fft(yfilt))  # FFT do vetor Y filtrado
Yfilt = Yfilt[0:len(Yfilt)/2]   # Pegar só a metade

t_limpo = plt.subplot(2, 2, 2, sharex=t_sujo)
plt.plot(t, yfilt)
plt.xlabel('Tempo (s)')
plt.xlim([0, t[-1]])
plt.ylabel('Amplitude (V)')
plt.title('Sinal limpo')

f_limpo = plt.subplot(2, 2, 4, sharex=f_sujo)
plt.plot(f, Yfilt)
plt.xlabel('f (Hz)')
plt.ylabel('Y')


minorLocator_t = AutoMinorLocator(n=10)
minorLocator_f = AutoMinorLocator(n=10)
majorLocator = AutoLocator()

t_sujo.xaxis.set_major_locator(majorLocator)
t_sujo.xaxis.set_minor_locator(minorLocator_t)
f_sujo.xaxis.set_minor_locator(minorLocator_f)

plt.tight_layout()
plt.show()
