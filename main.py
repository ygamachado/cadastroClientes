import cliente



op = 5
clientes = []


# Funcoes--------------------------------------------------
def menu():
    print("\n========================= Escolha uma opção ===========================")
    print("1-cadastrar cliente \n2-Listar Clientes \n3-Editar Divida\n0-sair")
    print("=======================================================================")


def inserir():
    print("Nome:")
    nome = input()
    print("CPF")
    cpf = input()
    print("Endereço")
    endereco = input()
    clienteOb = cliente.Cliente(nome, cpf, endereco)
    print("Deseja salvar? s/n:")
    salv = input()
    if (salv == "s"):
        salvar(clienteOb)


def salvar(clienteOb):
    clientes.append(clienteOb)
    print("==========================  Salvando....=====================================")
    print("-----------------------------------------------------------------------------")
    print("==========================  Salvo!  =========================================\n")


def listar():
    print(".........................Lista de Clientes...............................\n")
    for i in range(0, len(clientes)):
        clientes[i].imprimir()


def dividaAlterar():
    for i in range(len(clientes)):
        print("Cliente", i)
        clientes[i].imprimir()
    print("digite qual o cliente por numero")
    i = int(input())
    print("Digite o valor da divida")
    valor = int(input())
    clientes[i].valorDivida(valor)


# -------------------------Funcoes------------------------------
# Laço de Repetição e chamada das funcoes----------------------
while (op != 0):
    menu()
    op = int(input())
    if op == 1:
        inserir()
    elif op == 2:
        listar()
    elif (op == 3):
        dividaAlterar()
    elif (op == 0):
        break
