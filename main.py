#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

#programa usando uma lista com a idade e altura no mesmo vetor.

def carregarDadosIdadeAltura(n):
  dados = []
  idade = ' '
  altura = ' '
  for i in range(n):
    idade = int(input("Informe a idade: "))
    altura = float(input("Informa a altura: "))
    dados.append([idade, altura])
  return dados  
def exibirResulado(vetor):
  print(f'\nOs dados informados {vetor}')
  rev = list(reversed(vetor))
  print(f'\nOs dados em ordem inversa {rev} ')

  
vetor = carregarDadosIdadeAltura(5)
exibirResulado(vetor)