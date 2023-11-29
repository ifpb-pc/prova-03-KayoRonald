def soma_positivo(lista1, lista2):
  lista1_positivo = []
  lista2_positivo = []
  for i in lista1:
    if i > 0:
      lista1_positivo.append(i)
  for i in lista2:
    if i > 0:
      lista2_positivo.append(i)
  lista = lista1_positivo + lista2_positivo
  lista.sort()
  soma = 0
  for i in lista:
    soma += i
  return soma, lista