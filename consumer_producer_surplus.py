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

plt.fill_between(demand(p), p, eq_price, where=(p<=eq_price), color='blue', alpha=0.3)
plt.annotate('Konsumentenrente', (30, 30), xytext=(5, 5), textcoords='offset points')

plt.fill_between(supply(p), p, eq_price, where=(p<=eq_price), color='green', alpha=0.3)
plt.annotate('Produzentenrente', (30, 10), xytext=(5, 5), textcoords='offset points')

plt.xlabel('Menge')
plt.ylabel('Preis')
plt.title('Konsumenten- und Produzentenrente im Marktgleichgewicht')
plt.legend()
plt.grid(True)
plt.show()

def consumer_surplus(eq_price, eq_quantity):
    return 0.5 * (50 - eq_price) * eq_quantity

def producer_surplus(eq_price, eq_quantity):
    return 0.5 * (eq_price - 4) * eq_quantity

cs = consumer_surplus(20, 60)
ps = producer_surplus(20, 60)

print(f"Consumer Surplus: {cs:.2f}")
print(f"Producer Surplus: {ps:.2f}")
print(f"Total Economic Surplus: {cs + ps:.2f}")
