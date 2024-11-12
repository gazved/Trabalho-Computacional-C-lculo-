import matplotlib.pyplot as plt
from sympy import symbols, sympify, integrate, lambdify, pretty
import numpy as np

# Define the symbolic variable
x = symbols('x')

# Function to calculate the area using the Left Riemann sum
def riemann_left(f, g, a, b, n):
    dx = (b - a) / n
    area = 0
    for i in range(n):
        xi = a + i * dx
        height = abs(f(xi) - g(xi))
        area += height * dx
    return area

# Input and simplify the polynomial functions
polinomio1_input = input("Digite a primeira função polinomial: ")
polinomio2_input = input("Digite a segunda função polinomial: ")
f_expr = sympify(polinomio1_input)
g_expr = sympify(polinomio2_input)

# Display simplified functions
print("\nFunção 1 simplificada:")
print(pretty(f_expr))
print("Função 2 simplificada:")
print(pretty(g_expr))

# Convert expressions to numeric functions
f = lambdify(x, f_expr, 'numpy')
g = lambdify(x, g_expr, 'numpy')

# Input interval [a, b] and number of rectangles for Riemann sum
a = float(input("Digite o valor de 'a' (limite inferior): "))
b = float(input("Digite o valor de 'b' (limite superior): "))
n = int(input("Digite o número de retângulos para a soma de Riemann: "))

# Calculate the area using the Left Riemann sum
riemann_area = riemann_left(f, g, a, b, n)
print(f"\nÁrea usando soma de Riemann à esquerda: {riemann_area:.4f}")

# Calculate the area using the definite integral
integral_expr = abs(f_expr - g_expr)
integral_area = integrate(integral_expr, (x, a, b))
print(f"Área usando integral definida: {integral_area.evalf()}")

# Plot the functions and shaded area
x_vals = np.linspace(a, b, 400)
f_vals = f(x_vals)
g_vals = g(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x_vals, f_vals, label=f"f(x) = {f_expr}", color='blue')
plt.plot(x_vals, g_vals, label=f"g(x) = {g_expr}", color='green')

# Fill the area between the functions
plt.fill_between(x_vals, f_vals, g_vals, where=(f_vals > g_vals), color='skyblue', alpha=0.5)
plt.fill_between(x_vals, f_vals, g_vals, where=(g_vals > f_vals), color='lightcoral', alpha=0.5)

# Graph settings
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim([a, b])
plt.title("Área entre as funções")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
