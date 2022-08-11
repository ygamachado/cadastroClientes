import cliente
import bd_connector

conectar = bd_connector.DataBase()

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
    print("idade")
    idade = int(input())
    print("Endereco")
    endereco=input()
    clienteOb = cliente.Cliente(nome, cpf, idade,endereco)
    print("Deseja salvar? s/n:")
    salv = input()
    if (salv == "s"):
        salvar(clienteOb)
        conectar.cadastrar(nome,cpf,idade,endereco)
def salvar(clienteOb):
    clientes.append(clienteOb)
    clientes.append(conectar.leitura())
    print("==========================  Salvando....=====================================")
    print("-----------------------------------------------------------------------------")
    print("==========================  Salvo!  =========================================\n")


def listar():
    print(".........................Lista de Clientes...............................\n")
    #clientes.append(conectar.leitura())
    print(conectar.leitura())
    #for i in range(0, len(clientes)):
        #clientes[i]
        #print(clientes)



def dividaAlterar():
    print("digite qual o cliente por numero")
    i = int(input())
    print("Digite o valor da divida")
    valor = int(input())
    conectar.update(i,valor)

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
