##### Sistema de Login com Interface Gráfica eBanco de Dados ###


# criando um banco de dados e conectado nele
conexao = sqlite3.connect("tutorial.db")


# criando um cursor
cursor = conexao.cursor()


# criando a tabela do banco de dados
cursor.execute("""CREATE TABLE usuarios(
               id INTEGER PRIMARY KEY,
               nome_usuario TEXT NOT NULL ,
               senha TEXT NOT NULL 
               )
               """)


# função para cadastrar usuarios
def cadastra_usuario():

    id = input('Digite o id do usuário: ')
    nome_usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    
    cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?)", (id, nome_usuario, senha))
    conexao.commit()


# funcao para alterar usuarios
def altera_registro():

    id = input('Digite o id do usuário: ')
    nome_usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    
    cursor.execute("UPDATE usuarios SET nome_usuario = ?, senha = ? WHERE id = ?", (nome_usuario,senha, id))
    conexao.commit()


# funcao para excluir usuarios
def excluir_usuario():

    id = input('Digite o id do usuário a ser excluído: ')

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id))
    conexao.commit()


def retorna_usuario():

    id = input('Digite o id do usuário: ')
    nome_usuario = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')
    
    cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?)", (id, nome_usuario, senha))
    conexao.commit()





