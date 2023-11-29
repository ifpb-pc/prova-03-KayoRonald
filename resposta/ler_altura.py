def organizar_alturas(lista):
  lista_ordenada = []
  lista_ordenada.append(lista[1])
  lista_ordenada.append(lista[0])
  lista_ordenada.append(lista[2])
  return lista_ordenada

def formatar_alturas(lista):
  for i, altura in enumerate(lista):
    lista[i] = f'{altura:.2f}'
  return lista