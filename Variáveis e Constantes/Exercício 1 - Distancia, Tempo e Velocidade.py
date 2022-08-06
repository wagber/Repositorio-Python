'''
Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem,
utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário
deve fornecer o tempo gasto na viagem e a velocidade média durante ela.
Desta forma, será possível obter a distância percorrida com a fórmula
DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a
quantidade de litros de combustível utilizada na viagem, com a fórmula:
LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média,
tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem.
'''

tempo = float(input('O tempo da viagem em horas é: '))
velocidade = float(input('A velocidade do veículo na viagem foi: '))
km_litro = float(input('Meu veículo faz por quilometro um total em litros de combustível de: '))
print(f'O tempo da viagem foi {tempo} horas, a uma velocidade média de {velocidade} Km/h')
distancia = tempo * velocidade
litros_usados = round((distancia / km_litro),2)
print(f'A distância percorrida foi de {distancia} Km e a quantidade de litros utilizada'
      f'nessa viagem foi de {litros_usados}')