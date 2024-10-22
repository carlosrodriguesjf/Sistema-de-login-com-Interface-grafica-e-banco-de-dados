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



conexao = sqlite3.connect("tutorial.db")



