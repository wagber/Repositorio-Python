'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel
que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a
velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula
DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de
combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar
os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros
utilizada na viagem
'''

#Função para ler os valores (não recebe parâmetro e retorna os dois valores)
def ler_valores():
  a = float(input('Digite o valor do tempo da viagem: '))
  b = float(input('Digite a velocidade média: '))
  return a, b

#Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
def distancia(t, v):
  d = t * v
  return d
  #Ou podemos retorar direto
  #return t * v sem precisar fazer d = t * v

#Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
def consumo(distancia):
  litros_usados = distancia / 12
  return litros_usados

#Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
def resultado(velocidade, tempo, distancia, consumo):
  print(f'a velocidade é: {velocidade}, o tempo foi: {tempo}, a distancia foi: {distancia},'
        f'e o consumo foi: {consumo}')

#OU
def imprime_resultado(velocidade, tempo, distancia, litros):
  print('Velcidade: ', velocidade)
  print('Tempo: ', tempo)
  print('Distância: ', distancia)
  print('Litros: ', litros)

#Chamando as Funções

#Forma 1 de chamar as Funções
recebendo_valores = ler_valores()
calculando_distancia = distancia(recebendo_valores[0],recebendo_valores[1])
calculando_consumo = consumo(calculando_distancia)
print(f'O tempo da viagem é de {recebendo_valores[0]} horas')
print(f'com uma velocidade média de {recebendo_valores[1]} quilometro por hora')
print(f'e um consumo de {calculando_consumo} litros por quilometro para uma distancia de {calculando_distancia} quilometros.')
resultado(recebendo_valores[0],recebendo_valores[1],calculando_distancia, calculando_consumo)

#Forma 2 de chamar as Funções
t, v = ler_valores()
d = distancia(t, v)
l = consumo(d)
imprime_resultado(t, v, d, l)