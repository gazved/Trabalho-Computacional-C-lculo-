from sympy import symbols, sympify, integrate
import numpy as np

# Definir a variável simbólica
x = symbols('x')

# Instruções ao usuário
print('Instruções para utilizar: ' + '\n' + 'Digite o número e caso tenha um expoente, digite * e o expoente.')

# Ler o polinômio do usuário
polinomio_input = input("Digite sua função polinomial aqui: ")
polinomio = sympify(polinomio_input)

# Simplificar e ordenar o polinômio
polinomio = polinomio.simplify()
print("\nPolinômio simplificado e ordenado:")
print(polinomio)

# Calcular a integral indefinida
integral_indefinida = integrate(polinomio, x)
print("\nIntegral indefinida da função f(x):")
print(f"∫ f(x) dx = {integral_indefinida} + C")

# Perguntar ao usuário se deseja calcular uma integral definida
resposta = input("\nDeseja calcular uma integral definida? (Sim/Não): ").strip().lower()
if resposta == 'sim':
    try:
        # Obter os limites de integração
        a = float(input("Digite o limite inferior 'a': "))
        b = float(input("Digite o limite superior 'b': "))

        # Calcular a integral definida
        integral_definida = integrate(polinomio, (x, a, b))
        print(f"\nIntegral definida de f(x) de {a} até {b}:")
        print(f"∫[{a},{b}] f(x) dx = {integral_definida}")
    except ValueError:
        print("Por favor, digite valores numéricos válidos para 'a' e 'b'.")
