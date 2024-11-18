import matplotlib.pyplot as plt
import numpy as np

def price(q):
    return 100 - q

def revenue(q):
    return q * price(q)

def cost(q):
    return 20 + 10*q

def profit(q):
    return revenue(q) - cost(q)

q = np.linspace(0, 100, 1000)

plt.figure(figsize=(12, 8))

plt.plot(q, revenue(q), label='Erlös')
plt.plot(q, cost(q), label='Kosten')
plt.plot(q, profit(q), label='Gewinn')

q_max = q[np.argmax(profit(q))]
profit_max = profit(q_max)

plt.plot(q_max, profit_max, 'ro', label='Gewinnmaximum')
plt.annotate(f'Max ({q_max:.1f}, {profit_max:.1f})', (q_max, profit_max), xytext=(5, 5), textcoords='offset points')

plt.xlabel('Menge')
plt.ylabel('Wert')
plt.title('Erlösmaximierung und Gewinnmaximum')
plt.legend()
plt.grid(True)
plt.show()
