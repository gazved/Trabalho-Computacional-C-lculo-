import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify, pretty
import numpy as np

# Definir a variável simbólica
x = symbols('x')

# Instruções ao usuário
print('Instruções para utilizar:   ' + '\n' + 'Digite o número e caso tenha um expoente, digite * e o expoente.')

# Ler o polinômio do usuário
polinomio_input = input("Digite sua função polinomial aqui: ")
polinomio = sympify(polinomio_input)

# Simplificar e ordenar o polinômio
polinomio = polinomio.simplify()
print("\nPolinômio simplificado e ordenado:")
print(pretty(polinomio))

# Converter o polinômio para uma função utilizável numericamente
f = lambdify(x, polinomio, 'numpy')

# Lista para armazenar os valores de 'a' e f(a)
valores_a = []
valores_fa = []

# Perguntar se deseja calcular valor funcional
resposta = input("\nDeseja calcular valor funcional nas funções? (Sim/Não): ").strip().lower()
if resposta == 'sim':
    count = 0
    while count < 5:
        valor_a = input("\nQual o valor de 'a'? (Digite 'sair' para parar): ")
        if valor_a.lower() == 'sair':
            break
        try:
            # Convertendo o valor de 'a' para float e calculando o valor funcional
            valor_a = float(valor_a)
            valor_fa = f(valor_a)
            print(f"a = {valor_a}, f({valor_a}) = {valor_fa}")
            valores_a.append(valor_a)
            valores_fa.append(valor_fa)
            count += 1
        except ValueError:
            print("Por favor, digite um número válido para 'a'.")

# Plotando o gráfico no plano cartesiano
if valores_a:
    plt.figure(figsize=(6, 6))

    # Gerar valores de x para o gráfico
    x_vals = np.linspace(-6, 6, 400)
    y_vals = f(x_vals)

    # Plotar o gráfico da função polinomial
    plt.plot(x_vals, y_vals, label=f"f(x) = {polinomio}")

    # Plotar os pontos calculados
    plt.scatter(valores_a, valores_fa, color='red')

    # Adicionar rótulos nos pontos
    for i, (a, fa) in enumerate(zip(valores_a, valores_fa)):
        plt.text(a, fa, f"({a}, {fa})", fontsize=12, ha='right')

    # Configurações do gráfico
    plt.xlim([-6, 6])
    plt.ylim([-6, 6])
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.grid(True)
    plt.title("Gráfico da função polinomial e pontos calculados")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()

    # Mostrar o gráfico
    plt.show()
