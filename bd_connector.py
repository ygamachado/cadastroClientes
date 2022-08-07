import mysql.connector


class DataBase():
    db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="cad_bd")
    cursor = db_connection.cursor()


# CRUD
    # Create
    def cadastrar(self,cursor):
        login="admin1"
        senha="12345"
        nome="Pedro"
        comando = f'INSERT INTO `cad_bd`.`usuario` (`login`, `senha`) VALUES ("{login}","{senha}")'
        cursor.execute()
        self.cursor.execute(comando)

# read
    def leitura(self,cursor):
        comando = 'SELECT * FROM cad_bd.usuario'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()  # ler o banco
        print(resultado)

    # comando = 'SELECT * FROM cad_bd.usuario'
# cursor.execute(comando)
# resultado=cursor.fetchall()#ler o banco
# db_connection.commit()#edita o banco de dados
# print(resultado)


    cursor.close()
    db_connection.close()

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