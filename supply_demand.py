import matplotlib.pyplot as plt
import numpy as np

def demand(p):
    return 100 - 2*p

def supply(p):
    return 5*p - 20

p = np.linspace(0, 50, 100)

plt.figure(figsize=(10, 6))
plt.plot(demand(p), p, label='Nachfrage')
plt.plot(supply(p), p, label='Angebot')

eq_price = 20
eq_quantity = demand(eq_price)
plt.plot(eq_quantity, eq_price, 'ro', label='Gleichgewicht')
plt.annotate(f'({eq_quantity}, {eq_price})', (eq_quantity, eq_price), xytext=(5, 5), textcoords='offset points')

plt.xlabel('Menge')
plt.ylabel('Preis')
plt.title('Angebot und Nachfrage')
plt.legend()
plt.grid(True)
plt.show()
