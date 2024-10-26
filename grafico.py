from matplotlib import pyplot as plt

eixo_x_dias= [1,5,10,15,20,25,30]
eixo_y_temp_max = [28,29,25,32,34,36,40]
eixo_y_temp_min = [21,22,17,23,23,24,20]

plt.title(' Temperatura máxima e mínima ')
plt.xlabel('Dias')
plt.ylabel('temperatura')
plt.plot(eixo_x_dias, eixo_y_temp_max)
plt.plot(eixo_x_dias, eixo_y_temp_min)

plt.legend(['temperatura maxima', 'temperatura minima'])
plt.grid(True)

plt.show()