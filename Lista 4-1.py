#criação do arquivo
try:
  with open('pessoas.txt', 'r') as file:
    file.close()
    print(f"Arquivo {file.name} já existente")
except FileNotFoundError:
  #Arquivo não encontrado
  with open('pessoas.txt', 'x') as file:
    file.write('')
    file.close()
    print(f"Arquivo {file.name} criado!\n")

#Função de Menu + Escolha
def Escolha():
  print("1. Inserir pessoa\n", "2. Listar pessoas cadastradas\n",
        "3. Buscar pessoa por CPF\n", "4. Buscar pessoa por Telefone\n",
        "5. Remover pessoa por CPF\n", "6. SAIR\n")
  op = int(input("Insira a opção: "))
  while op > 6 or op < 0:
    op = int(input("Valor inválido! Digite novamente (0 a 6): "))
  return op

#verfica telefone existente
def SearchTelephone(telefone):
  file = open("pessoas.txt", 'r')
  for linha in file:
    if telefone in linha:
      print("Número de telefone já cadastrado!\n")
      file.close()
      return True
  file.close()
  return False

#verifica cpf existente
def SearchCPF(cpf):
  file = open("pessoas.txt", 'r')
  for linha in file:
      if linha.startswith(f"CPF: {cpf}"):
          print("CPF já cadastrado!\n")
          file.close()
          return True
  file.close()
  return False

#coleta os dados do usuário
def LerDadosPessoa():
  num = input("Digite o CPF do usuário: ")
  
  if SearchCPF(num) == True:
    print("CPF JÁ CADASTRADO!Operação Cancelada!")
    return
  
  cpf = num
  nome = input("Digite o nome do usuário: ")
  endereco = input("Digite o endereço do usuário: ")
  telefones = input("Digite os telefones(separados por vírgulas): ")
  while SearchTelephone(telefones) == True:
    telefones = input("Telefone já cadastrado! Insira novamente(separado por vírgulas): ")
  pessoa = f"CPF: {cpf} | Nome: {nome} | Endereço: {endereco} | Telefone(s): {telefones} \n"
  print("\n")
  return pessoa

#Insere os dados coletados dentro do arquivo
def Insere(pessoa):
  file = open("pessoas.txt", 'a')
  file.write(pessoa)
  file.close()
  print("Cadastro realizado com sucesso!")

#mostra as pessoas cadastradas
def Listagem():
  file = open("pessoas.txt","r")
  conteudo = file.read()
  if conteudo.find(f"CPF: ") == -1:
    print("Lista Vazia!")
    return
  print(conteudo)
  file.close()

#sobrescreve dados no arquivo
def DataEraser():
  file = open("pessoas.txt", 'w')
  file.write("")
  file.close

#busca pessoas pelo cpf
def BuscarPeloCPF(cpf):
  file = open("pessoas.txt", 'r')
  for linha in file:
    if cpf in linha:
      print("Pessoa encontrada")
      print(linha)
  file.close()

#busca pessoas pelo Telefone
def BuscarPeloTelefone(telefone):
  file = open("pessoas.txt", 'r')
  for linha in file:
    if telefone in linha:
      print(linha)

#remove pessoas pelo cpf
def RemoverPessoa(cpf):
  file = open("pessoas.txt", 'r')
  cont = ''
  for linha in file:
    if (f"CPF: {cpf}") in linha:
      linha =''
      print("Pessoa removida com sucesso!\n")
    cont = cont + linha  
  file.close()
  file2 = open("pessoas.txt", 'w')
  file2.write(cont)
  file2.close()

while(True):
  escolha = Escolha()
  
  if escolha == 6:
    print("Programa Encerrado!")
    break
  
  elif escolha == 1:
    pessoa = LerDadosPessoa()
    if pessoa != None:
      Insere(pessoa)
      
  elif escolha == 2:
    Listagem()

  elif escolha == 3:
    num = input("Digite o CPF da pessoa buscada: ")
    BuscarPeloCPF(num) 

  elif escolha == 4:
    tel = input("Digite o nº de telefone a ser buscado: ")
    BuscarPeloTelefone(tel)

  elif escolha == 5:
    num = input("Número do CPF a ser retirado da lista: ")
    RemoverPessoa(num)