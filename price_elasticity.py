import matplotlib.pyplot as plt
import numpy as np

def demand(p):
    return 100 - 2*p

p = np.linspace(0, 50, 100)
q = demand(p)

plt.figure(figsize=(10, 6))
plt.plot(q, p, label='Nachfrage')

p1, p2 = 20, 30
q1, q2 = demand(p1), demand(p2)

elasticity = ((q2-q1)/q1) / ((p2-p1)/p1)

plt.plot([q1, q2], [p1, p2], 'ro-', label=f'Elastizität: {elasticity:.2f}')

plt.annotate(f'P1({q1}, {p1})', (q1, p1), xytext=(5, 5), textcoords='offset points')
plt.annotate(f'P2({q2}, {p2})', (q2, p2), xytext=(5, 5), textcoords='offset points')

plt.xlabel('Menge')
plt.ylabel('Preis')
plt.title('Preiselastizität der Nachfrage')
plt.legend()
plt.grid(True)
plt.show()
