'''
Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar
todos os elementos da matriz

matriz = np.array([[3, 4, 1], [3, 1, 5]])
'''

#Primeiramente, quando vamos trabalhar com Array temos que importar a biblioteca Numpy
import numpy as np

#Criando uma matriz conforme solicitada na questão:
matriz = np.array([[3,4,1],[3,1,5]])
print(matriz)

#Primeiramente, quando vamos trabalhar com Array temos que importar a biblioteca Numpy
import numpy as np

#Criando uma matriz conforme solicitada na questão:
matriz = np.array([[3,4,1],[3,1,5]])
print(f'A matriz criada é: ')
print(matriz)
print('------------------------------------')

#Criando uma estrutura de repetição para percorrer e somar todos os alementos da matriz
soma_matriz = 0
for i in range(matriz.shape[0]):
  print(matriz[i])
  print(' ')
  for j in range(matriz.shape[1]):
    print(matriz[i][j])
    print('----')
    print(' ')
    soma_matriz += matriz[i][j]
print(f'A soma de todos os valores da matriz é igual a {soma_matriz}')

