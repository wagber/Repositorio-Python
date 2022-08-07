'''
Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos
valores por meio de uma estrutura de repetição. Depois, crie uma nova estrutura de repetição para
somar todas as notas e retornar a média.
'''

#Nessa estrutura a lógica usada foi: Para cada 3 loops de i 1 loop para j
boletim_notas = {}
for i in range(3):
  nome = input(f'Digite o nome do {i + 1}º aluno ')
  for j in range(1):
    nota = float(input(f'Digite a nota do {i + 1}º aluno '))
  boletim_notas[nome] = nota
print(boletim_notas)

#Contudo temos uma forma bem mais simples e objetiva
alunos = {}
for _ in range(1, 4):
  nome = input('Digite o nome de um aluno ')
  nota = float(input('Digite a nota de um aluno '))
  alunos[nome] = nota
print(alunos)

#Apresentando o dicionário criado
print(f'O dicionário boletim_notas é {boletim_notas}.')
#Mostrando o tamanho do dicionário
tamanho_dicionario = (len(boletim_notas))
print(f'Seu tamanho é de {tamanho_dicionario} posições.')
#Fazendo a soma e a média dos valores contidos no dicionário por meio de uma estrutura de repetição FOR
soma = 0
for i in boletim_notas.values():
  soma = float(soma + i)
media = round(float(soma / tamanho_dicionario),2)
#Imprimindo o valor da soma e da média
print(f'A soma das notas é igual a {soma} e a sua média é igual {media}')