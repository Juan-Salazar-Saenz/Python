import random

def imprimir(x, y):
  posibles = ['C', 'S']
  valores = []
  for i in range(0, y):
    valores.append(random.choice(posibles))
  print(valores)
  return valores.count(x)

def imprimir2(y):
  posibles = ['C', 'S']
  valores = []
  for i in range(0, y):
    valores.append(random.choice(posibles) + random.choice(posibles))
  print(valores)
  print("CC -> ",(valores.count('CC') / y))
  print("CS -> ",(valores.count('CS') / y))
  print("SC -> ",(valores.count('SC') / y))
  print("SS -> ",(valores.count('SS') / y))