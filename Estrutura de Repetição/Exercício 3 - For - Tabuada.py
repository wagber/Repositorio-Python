'''
Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
'''

#Usando For - Forma 1

for i in range(11):
  mult = 3 * i
  print(f'3 x {i} = {mult}')

'''

#Usando For - Forma 2

for i in range(1,11):
  print('3 x {} = {}'.format(i, 3 * i))

'''