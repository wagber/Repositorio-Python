'''
Leia a idade do usuário e classifique-o em:

Criança – 0 a 12 anos
Adolescente – 13 a 17 anos
Adulto – acima de 18 anos

Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
'''

idade = int(input('Digite a sua idade '))

if idade >= 0 and idade <= 12:
  print(f'A Criança tem {idade} anos')
elif idade > 12 and idade <= 18:
  print(f'O Adolescente tem {idade} anos')
elif idade > 18 and idade <= 130:
  print(f'O Adulto tem {idade} Anos')
elif idade < 0  or idade > 130:
  print(f'Idade inválida')