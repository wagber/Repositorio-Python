'''
Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas
M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se
o aluno foi aprovado, reprovado ou pegou exame.

Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
Se a média for maior do que 6.0, o aluno está aprovado
Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0,
está aprovado, senão; está reprovado
'''

M1 = float(input('Digite a nota 1 '))
M2 = float(input('Digite a nota 2 '))
M3 = float(input('Digite a nota 3 '))

media = round(((M1 + M2 + M3) / 3), 2)
print(media)

if media >= 0.0 and media <= 4.0:
  print('Aluno foi Reprovado')
elif media > 4.1 and media <= 6.0:
  exame = float(input('Digite a nota do exame '))
  if exame >= 6.0:
      print('Aprovado no Exame')
  else:
      print('Reprovado no Exame')
elif media < 0:
  print('Nota inválida')
else:
  print('Aluno Aprovado')