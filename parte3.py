import matplotlib.pyplot as plt
from sympy import symbols, sympify, integrate, lambdify, pretty
import numpy as np


x = symbols('x')


def riemann_left(f, g, a, b, n):
    dx = (b - a) / n
    area = 0
    for i in range(n):
        xi = a + i * dx
        height = abs(f(xi) - g(xi))
        area += height * dx
    return area


polinomio1_input = input("Digite a primeira função polinomial: ")
polinomio2_input = input("Digite a segunda função polinomial: ")
f_expr = sympify(polinomio1_input)
g_expr = sympify(polinomio2_input)


print("\nFunção 1 simplificada:")
print(pretty(f_expr))
print("Função 2 simplificada:")
print(pretty(g_expr))


f = lambdify(x, f_expr, 'numpy')
g = lambdify(x, g_expr, 'numpy')


a = float(input("Digite o valor de 'a' (limite inferior): "))
b = float(input("Digite o valor de 'b' (limite superior): "))
n = int(input("Digite o número de retângulos para a soma de Riemann: "))


riemann_area = riemann_left(f, g, a, b, n)
print(f"\nÁrea usando soma de Riemann à esquerda: {riemann_area:.4f}")


integral_expr = abs(f_expr - g_expr)
integral_area = integrate(integral_expr, (x, a, b))
print(f"Área usando integral definida: {integral_area.evalf()}")


x_vals = np.linspace(a, b, 400)
f_vals = f(x_vals)
g_vals = g(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, f_vals, label=f"f(x) = {f_expr}", color='blue')
plt.plot(x_vals, g_vals, label=f"g(x) = {g_expr}", color='green')


plt.fill_between(x_vals, f_vals, g_vals, where=(f_vals > g_vals), color='skyblue', alpha=0.5)
plt.fill_between(x_vals, f_vals, g_vals, where=(g_vals > f_vals), color='lightcoral', alpha=0.5)


plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([a, b])
plt.title("Área entre as funções")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
