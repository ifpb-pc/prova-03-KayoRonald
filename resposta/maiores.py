def maiores(cidades):
  maiores = []
  for pessoa in cidades:
    idades_cidades  = cidades[pessoa]
    if idades_cidades > 100:
      maiores.append(pessoa)
  return maiores