import matplotlib.pyplot as plt
import numpy as np

def demand(q):
    return 10 - 0.5*q

def supply(p):
    return 2*p - 2

p = np.linspace(0, 10, 100)
q = np.linspace(0, 20, 100)

plt.figure(figsize=(10, 6))
plt.plot(q, demand(q), label='Nachfrage')
plt.plot(supply(p), p, label='Angebot')

p_start = 8
q_start = supply(p_start)
steps = 6

for i in range(steps):
    p_next = demand(q_start)
    q_next = supply(p_next)
    
    plt.plot([q_start, q_start], [p_start, p_next], 'r-')
    plt.plot([q_start, q_next], [p_next, p_next], 'r-')
    
    p_start, q_start = p_next, q_next

plt.xlabel('Menge')
plt.ylabel('Preis')
plt.title('Spinnwebprinzip')
plt.legend()
plt.grid(True)
plt.show()
