import mysql.connector
import cliente

class DataBase():
    db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="cad_bd")


# CRUD
    # Create
    def cadastrar(self,nome,cpf,idade,endereco):
        divida=0
        id_usuario = 1
        cursor = self.db_connection.cursor()
        #comando = f'INSERT INTO `cad_bd`.`cliente` (`nome`, `senha`) VALUES ("{login}","{senha}")'
        comando = f'INSERT INTO `cad_bd`.`cliente`' \
                  f' (`nome`, `cpf`, `divida`, `idade`, `endereco`, `id_usuario`) ' \
                  f'VALUES ("{nome}", "{cpf}","{divida}", "{idade}", "{endereco}", "{id_usuario}")'
        cursor.execute(comando)
        self.db_connection.commit()
        cursor.close()
        #self.db_connection.close()
# read
    def leitura(self):
        clientes=[]
        cursor = self.db_connection.cursor()
        comando = 'SELECT * FROM cad_bd.cliente'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco
        return(resultado)
        cursor.close()



        #self.db_connection.close()
# update
    def update(self,id,divida):
        cursor = self.db_connection.cursor()
        comando = f'UPDATE cad_bd.cliente SET divida = "{divida}" WHERE (id_cliente = "{id}");'
        cursor.execute(comando)
        self.db_connection.commit()
        cursor.close()
        #self.db_connection.close()
# delete
    def delete(self,id):
        cursor = self.db_connection.cursor()
        comando = f'DELETE FROM `cad_bd`.`cliente` WHERE (`id_cliente` = "{id}");'
        cursor.execute(comando)
        self.db_connection.commit()
        cursor.close()
        #self.db_connection.close()
    # comando = 'SELECT * FROM cad_bd.usuario'
    def encerrar(self):
        self.db_connection.close()
# cursor.execute(comando)
# resultado=cursor.fetchall()#ler o banco
# db_connection.commit()#edita o banco de dados
# print(resultado)



# CREATE

# nome_produto = "chocolate"

# valor = 15

# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados



# READ

# comando = f'SELECT * FROM vendas'

# cursor.execute(comando)

# resultado = cursor.fetchall() # ler o banco de dados

# print(resultado)



# UPDATE

# nome_produto = "todynho"

# valor = 6

# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados



# DELETE

# nome_produto = "todynho"

# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados