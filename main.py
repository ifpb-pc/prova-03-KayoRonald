from resposta.maiores import maiores
from resposta.processa_lista import processa_lista
from resposta.soma_positivo import soma_positivo
from resposta.ler_altura import organizar_alturas, formatar_alturas
def q1(cidades):
  """
    A partir do dicionário de nomes e idades de cidades a seguir, 
    crie uma função que retorne uma lista de cidades maiores que 100 anos.
  """
  respostas = maiores(cidades)
  return respostas

def q2(lista1, lista2):
  soma, lista = soma_positivo(lista1, lista2)
  return soma, lista

def q3(valores):
  pares, impares = processa_lista(valores)

  return pares, impares

def q4(valores):
    organizar = organizar_alturas(valores)
    formatar = formatar_alturas(organizar)
    return formatar


def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultQ1 = q1(idades)
    print("Questão 01:", resultQ1)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resulltQ2 = q2(lista1, lista2)
    print("Questão 02: ", resulltQ2)

    resultQ3 =  [2, 4, 6, 8, 10, 12, 1, 3, 5, 7, 9, 11, 0]
    print("Questão 03: ", q3(resultQ3))

    resultQ4 = q4(valores = [30, 20, 10])
    print("Questão 04: ", resultQ4)



if __name__ == "__main__":
    main()

    