'''
1 - Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit.
A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e
C é a temperatura em graus Celsius.
'''

#Função para ler e retorna o valor da temperatura (não recebe parâmetro)

def ler_temperatura():
  temperatura_Celsius = float(input('Digite a temperatura em graus Celsius: '))
  return temperatura_Celsius

#Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)

def converter_temperatura(temperatura_em_Celsius):
  temperatura_em_Fahrenheit = ((9 * temperatura_em_Celsius) + 160) / 5
  return temperatura_em_Fahrenheit

#Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão

def mostrar_resultado(temperatura_Fahrenheit):
  print(temperatura_Fahrenheit)

#Chamando as Funções

temperatura_c = ler_temperatura()
temperatura_f = converter_temperatura(temperatura_c)
mostrar_resultado = (temperatura_f)
print(mostrar_resultado)