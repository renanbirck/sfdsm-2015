%%% Exemplo de projeto de filtro digital com o Octave
%%%
%%% Se ele falhar ao rodar é por que você não tem os
%%% pacotes 'control' e 'signal'.
%%%
%%% Nesse caso execute 'pkg install control -forge' e
%%% 'pkg install signal -forge' no Octave.

pkg load signal;    % Carrega o pacote de processamento de sinal

Fs = 1000;      % Taxa de amostragem do sinal (Hz)
Ts = 1/1000;    % Tempo de amostra

t = 0:Ts:1;
Forig = 60;     % Frequência do sinal original
Fdirty1 = 120;    % Frequência do "ruído" no sinal
Fdirty2 = 200;  % Frequência do "ruído" no sinal

yorig = sin(2*pi*Forig*t);
y = yorig + 0.5*sin(2*pi*Fdirty1*t) + 0.8*sin(2*pi*Fdirty2*t);
Y = abs(fft(y));
Y = Y(1:length(Y)/2);

f = (0:length(Y)-1)*Fs/length(y);

t_sujo = subplot(2, 2, 1);   % Criar gráfico
plot(t, y);
xlabel('Tempo (s)');
xlim([0 t(end)]);
ylabel('Amplitude (V)');
title("Sinal sujo")

f_sujo = subplot(2, 2, 2);
plot(f, Y);
xlabel('f (Hz)');
ylabel('Y');
set(gca, 'xtick', 0:Fs/20:Fs/2)

% Limpeza do sinal

% Calcular coeficientes do filtro

Wc = 75 / (Fs/2)       % Frequencia de corte: 75 Hz
[b, a] = butter(6, Wc)  % Filtro de Butterworth, 6a ordem
yfilt = filtfilt(b, a, y);
Yfilt = abs(fft(yfilt));
Yfilt = Yfilt(1:length(Yfilt)/2);

t_limpo = subplot(2, 2, 3);   % Criar gráfico
plot(t, yfilt, 'r-', t, yorig, 'k-');
xlabel('Tempo (s)');
xlim([0 2*pi]);
ylabel('Amplitude (V)');
legend("Sinal filtrado", "Referência");
title("Sinal limpo")

f_limpo = subplot(2, 2, 4);
plot(f, Yfilt);
xlabel('f (Hz)');
ylabel('Y');
set(gca, 'xtick', 0:Fs/20:Fs/2)

linkaxes([t_sujo, t_limpo], 'x')
linkaxes([f_sujo, f_limpo], 'x')
