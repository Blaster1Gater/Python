import numpy as np
import sounddevice as sd

# Parâmetros para o som
frequencia = 440  # Frequência da onda em Hz (A4)
duracao = 0.1  # Duração em segundos
taxa_amostragem = 44100  # Taxa de amostragem (samples por segundo)

# Gerando uma onda senoidal
t = np.linspace(0, duracao, int(taxa_amostragem * duracao), endpoint=False)  # Tempo
onda = 0.5 * np.sin(2 * np.pi * frequencia * t)  # Fórmula da onda senoidal

# Reproduzindo o som
sd.play(onda, taxa_amostragem)
sd.wait()  # Aguarda até que o som termine de tocar

