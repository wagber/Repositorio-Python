'''
Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
para somar todos os valores digitados.
'''

#Forma 1

#Criando uma lista vazia
lista = []
#Criando uma estrutura de repetição para inserir valores dentro de uma lista
for i in range(5):
  numero = int(input(f'Digite o {i + 1}º número: '))
  lista.append(numero)
print(lista)

#Forma 1

print(f'Os valores da lista são {lista}')
soma = 0
#Criando estrutura de repetição para somar todos os valores de uma lista
for numeros in lista:
  soma += numeros
print(f'A soma da lista é = {soma}')

#-------------------------------------------------------------------------------------

#Forma 2

#Ou podemos fazer o mesmo for acima dessa forma:
#Criando uma lista vazia
lista2 = []
#Criando uma estrutura de repetição para inserir valores dentro de uma lista
for i in range(1, 6):
  numero = int(input(f'Digite o {i}º número: '))
  lista2.append(numero)
print(lista2)

#Forma 2

#Ou podemos fazer a soma dos números com o for sendo feito assim:
print(f'Os valores da lista são {lista2}')
soma2 = 0
#Criando estrutura de repetição usando o tamanho da lista com a função len para somar todos os valores de uma lista
for numeros in range(len(lista2)):
  soma2 += lista2[numeros]
print(f'A soma da lista é = {soma2}')

'''
Também podemos converter a lista para um ARRAY e assim termos acesso a algumas funções matemáticas.
Com isso podemos usar alguns recursos como soma, média, valor mínimo, valor máximo. 
Primeiro vamos importar a biblioteca Numpy
'''
import numpy as np
#agora vamos converter a lista para um array e usar a função SUM de soma.
soma3 = np.array(lista).sum()
print(soma3)
#O mesmo serve pra Forma 2
#soma4 = np.array(lista2).sum()
#print(soma4)