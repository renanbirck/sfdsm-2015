%%% Exemplo de transformada rápida de Fourier com o Octave.
%%%
%%%

Fs = 1000;     % Taxa de amostragem do sinal (Hz)
Ts = 1/Fs;      % Tempo entre amostras = 1/Fs

t = 0:Ts:2*pi;           % Vetor tempo
F1 = 10;                  % Primeira frequencia (Hz)
F2 = 50;                 % Segunda frequencia (Hz)
F3 = 100;                % Terceira frequencia (Hz)

y = sin(2*pi*F1*t) + sin(2*pi*F2*t) + sin(2*pi*F3*t); % y = sinal composto
Y = abs(fft(y));  % Y = fft do sinal (descartar fase)
Y = Y(1:length(Y)/2); % Descartar segunda metade (FFT eh simetrico)

f = (0:length(Y)-1)*Fs/length(y); % Vetor frequencia

subplot(211);    % Criar grafico
plot(t, y);      % plotar no dominio do tempo
xlabel('Tempo (s)');
xlim([0 2*pi]);  % Limitar o eixo X entre 0 e 2 pi
ylabel('Amplitude (V)');

subplot(212);
plot(f, Y);
xlabel('f (Hz)');
ylabel('Y');
set(gca, 'xtick', 0:Fs/20:Fs/2);    % Colocar "ticks" a cada 50 Hz
