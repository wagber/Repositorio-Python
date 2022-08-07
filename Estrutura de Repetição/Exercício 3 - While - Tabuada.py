'''
Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)
'''

# Usando While - Forma 1

taboada = -1
while taboada < 10:
    taboada += 1
    mult = 3 * taboada
    print(f'3 x {taboada} = {mult}')

'''

#Usando While - Forma 2

numero = 1
while numero <= 10:
  print('3 x {} = {}'.format(numero, 3 * numero))
  numero +=1

'''