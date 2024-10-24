##### Sistema de Login com Interface Gráfica eBanco de Dados ###


'''Funcionalidades que o projeto deve possuir:
1. Registro de Usuários:
○ Permitir que novos usuários se registrem com um nome de usuário e senha.
○ Armazenar o nome de usuário e a senha criptografada no banco de dados
SQLite.
2. Login de Usuários:
○ Permitir que os usuários façam login com suas credenciais (nome de usuário e
senha).
○ Verificar as credenciais no banco de dados SQLite.
3. Interface Gráfica:
○ Criar uma interface gráfica para o registro e login de usuários usando
CustomTkinter.
4. Banco de dados
○ Integre a criação, e validação de usuários e senha a um banco de dados
SQLite3
5. Entregar o resultado no formato de um executável
○ Entregue seu software no formato de um executável'''


# importações
# import customtkinter
import sqlite3

# app = customtkinter.CTk()
# app.geometry("400x300")
# app.title("Login")

# label = customtkinter.CTkLabel(app, text="CTkLabel", fg_color="transparent")




# app.mainloop()



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



