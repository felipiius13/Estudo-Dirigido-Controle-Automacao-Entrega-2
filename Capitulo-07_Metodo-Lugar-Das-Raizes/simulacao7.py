!pip install control

import control as ct
import numpy as np
import matplotlib.pyplot as plt

numerador = [1]
denominador = np.convolve([1, 0], np.convolve([1, 2], [1, 4])) # s(s+2)(s+4)
G = ct.tf(numerador, denominador)

print("Função de Transferência de Malha Aberta:")
print(G)

plt.figure(figsize=(10, 8))
ct.root_locus(G, plot=True, grid=True)

plt.title('Lugar das Raízes: Variação dos Polos com o Ganho K')
plt.axvline(0, color='r', linestyle='--', label='Fronteira de Estabilidade')
plt.legend()
plt.show()

print("Interpretação: Para ganhos baixos, o sistema é lento (polos perto da origem).")
print("Para ganhos médios, o sistema oscila mas é estável.")
print("Para ganhos muito altos, os ramos cruzam para a direita e o sistema fica instável.")
