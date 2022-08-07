'''
Ler 5 notas e informar a média
'''
#Usando For

soma = 0
#A variável nota aqui está consumindo memória. Se fosse penas o _ não estaria consumindo
for nota in range(5):
  nota = float(input('Digite a nota '))
  soma += nota
print(round((soma / 5),1))

nota = media = soma = 0
#Aqui como não vamos usar a variável então usamos o _ para não consumir memória
for _ in range (1,6):
  nota = float(input('Digite a nota '))
  soma += nota
print(soma)
media = round((soma / 5),1)
print(f'A média é {media}')