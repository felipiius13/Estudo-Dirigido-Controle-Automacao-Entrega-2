import control as ct
import numpy as np
import matplotlib.pyplot as plt

G = ct.tf([1], [1, 10, 20])

t = np.linspace(0, 4, 1000)
_, y_open = ct.step_response(G, t)

Kp = 300
Ki = 500
Kd = 10
Ctrl_PID = ct.tf([Kd, Kp, Ki], [1, 0])

L = Ctrl_PID * G
T_pid = ct.feedback(L, 1)
_, y_pid = ct.step_response(T_pid, t)

plt.figure(figsize=(12, 6))
plt.plot(t, y_open, 'r--', label='Malha Aberta (Lento, Erro alto)')
plt.plot(t, y_pid, 'b-', label='Com PID (Rápido, Erro Zero)')
plt.axhline(1, color='k', linestyle=':', label='Referência (Setpoint)')
plt.title('Comparação: Planta Original vs. Controlada com PID')
plt.xlabel('Tempo (s)')
plt.ylabel('Saída')
plt.legend()
plt.grid()
plt.show()

info = ct.step_info(T_pid)
print(f"Sobressinal com PID: {info['Overshoot']:.2f}%")
print(f"Tempo de Acomodação com PID: {info['SettlingTime']:.2f}s")
