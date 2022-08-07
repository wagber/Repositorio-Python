'''
Ler 5 notas e informar a média
'''

#Usando WHILE

soma = 0
quant_notas = 1
while quant_notas < 6:
  nota = float(input(('Digite uma nota ')))
  quant_notas +=1
  soma += nota
print(round((soma / 5),1))