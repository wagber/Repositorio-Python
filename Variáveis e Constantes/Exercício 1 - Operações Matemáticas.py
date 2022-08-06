'''Ler dois números inteiros, executar e mostrar o resultado das seguintes operações:
adição, subtração, multiplicação e divisão is None:
'''

a = int(input('Digite um número para A '))
b = int(input('Digite um número para B '))
#----------------------------------------
print(f'O valor de a é {a} e o valor de b é {b}')
#----------------------------------------
print('A soma de a + b é =',a + b)
print('A subtração de a - b é =',a - b)
print('A multiplicação de a * b é =',a * b)
print('A divisão de a / b é =',round((a / b),2))
#-----------------------------------------
adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = round((a / b),2)

print(f'A soma de a + b é = {adicao}')
print(f'A subtração de a - b é = {subtracao}')
print(f'A multiplicação de a * b é = {multiplicacao}')
print(f'A divisão de a / b é = {divisao}')