from sympy import symbols, pprint, sympify

# Definir a variável simbólica
x = symbols('x')

print('Instruções para utilizar:   '+ 'n' + 'digite o número e caso tenha um expoente digite * e o expoente')

polinomio_input = input("Digite sua função polinomial aqui: ")
polinomio = sympify(polinomio_input)


# Imprimir o polinômio de forma legível
pprint(polinomio)
