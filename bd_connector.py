import mysql.connector


class DataBase():



# CRUD
    # Create
    def cadastrar(self,cursor):
        login="admin1"
        senha="12345"
        nome="Pedro"
        comando = f'INSERT INTO `cad_bd`.`usuario` (`login`, `senha`) VALUES ("{login}","{senha}")'
        self.cursor.execute(comando)
        self.db_connection.commit()
# read
    def leitura(self):
        db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="cad_bd")
        cursor = db_connection.cursor()
        comando = 'SELECT * FROM cad_bd.usuario'
        cursor.execute(comando)
        resultado = cursor.fetchall()  # ler o banco
        print(resultado)

        cursor.close()
        db_connection.close()
# update
    def update(self,login,senha):
        comando = f'UPDATE `cad_bd`.`usuario` SET(`login`, `senha`) = ("{login}","{senha}") WHERE login = {login}'
        self.cursor.execute(comando)
        self.db_connection.commit()

# delete
    def delete(self,login):
        comando = f'DELETE FROM`cad_bd`.`usuario` WHERE `login` = "{login}"'

    # comando = 'SELECT * FROM cad_bd.usuario'
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