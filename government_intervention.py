import matplotlib.pyplot as plt
import numpy as np

def demand(p):
    return 100 - 2*p

def supply(p):
    return 5*p - 20

p = np.linspace(0, 50, 100)

plt.figure(figsize=(12, 8))
plt.plot(demand(p), p, label='Nachfrage')
plt.plot(supply(p), p, label='Angebot')

eq_price = 20
eq_quantity = demand(eq_price)
plt.plot(eq_quantity, eq_price, 'ro', label='Gleichgewicht')
plt.annotate(f'({eq_quantity}, {eq_price})', (eq_quantity, eq_price), xytext=(5, 5), textcoords='offset points')

price_ceiling = 15
plt.axhline(y=price_ceiling, color='r', linestyle='--', label='Preisobergrenze')
plt.fill_between(p, price_ceiling, p, where=(p>price_ceiling), color='red', alpha=0.3)
plt.annotate('Nachfrageüberschuss', (demand(price_ceiling), price_ceiling), xytext=(5, 5), textcoords='offset points')

price_floor = 25
plt.axhline(y=price_floor, color='g', linestyle='--', label='Preisuntergrenze')
plt.fill_between(p, price_floor, p, where=(p<price_floor), color='green', alpha=0.3)
plt.annotate('Angebotsüberschuss', (supply(price_floor), price_floor), xytext=(5, 5), textcoords='offset points')

plt.xlabel('Menge')
plt.ylabel('Preis')
plt.title('Auswirkungen staatlicher Eingriffe auf das Marktgleichgewicht')
plt.legend()
plt.grid(True)
plt.show()
