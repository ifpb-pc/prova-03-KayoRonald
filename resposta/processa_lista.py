def processa_lista(lista):
  pares = []
  impares = []
  for i in lista:
    if i == 0:
      break
    if i % 2 == 0:
      pares.append(i)
    else:
      impares.append(i)

  return pares, impares