listaNomes = []
listaCargos = []
listaNascimento = []
listaPlantoes = []
listaApos2000 = []
qtdeMedicos = 0
qtdeEnfermeiros = 0
qtdeAntes1990 = 0
maiorPlantao = 0
nomeMaiorPlantao = ""

for i in range(2):
  nome = input("Informe seu nome: ")
  listaNomes.append(nome)
  cargo = input("Informe seu cargo: ")
  listaCargos.append(cargo)
  anoNascimento = int(input("Informe o ano de nascimento: "))
  listaNascimento.append(anoNascimento)
  qtdePlantoes = int(input("Informe a quantidade de plantões: "))
  listaPlantoes.append(qtdePlantoes)

  if (cargo.lower() == "médico" or cargo.lower() == "medico"):
    qtdeMedicos += 1
  elif (cargo.lower() == "enfermeiro" or cargo.lower() == "enfermeira"):
    qtdeEnfermeiros += 1

  if (anoNascimento < 1990):
    qtdeAntes1990 += 1

  if (qtdePlantoes > maiorPlantao):
    maiorPlantao = qtdePlantoes
    nomeMaiorPlantao = nome

  if ( anoNascimento > 2000):
    listaApos2000.append(nome)


print(f"O total de médicos é: {qtdeMedicos}")
print(f"O total de enfermeiros é: {qtdeEnfermeiros}")
print(f"A quantidade de pessoas nascidas antes de 1990 é: {qtdeAntes1990}")
print(f"O funcionário com mais plantões foi o(a): {nomeMaiorPlantao} com {maiorPlantao} plantões")
print(f"A média de plantões é: {sum(listaPlantoes)/2}")
print(f"Os funcionários nascidos após 2000 é: {listaApos2000}")






