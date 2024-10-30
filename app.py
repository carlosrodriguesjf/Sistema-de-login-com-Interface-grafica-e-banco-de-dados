


import customtkinter as Ctk
import sqlite3



class CadastroFuncionarios(Ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def cadastro_usuarios():

            # Pega todo o texto do textbox
            nome_usuario = textbox_cadastro_usuario.get("1.0", "end").strip()  
            senha_usuario = textbox_cadastro_senha.get().strip()

            # criando um banco de dados e conectado nele
            conexao = sqlite3.connect("funcionarios.db")

            # criando um cursor
            cursor = conexao.cursor()

            # buscando o último id
            cursor.execute("SELECT * FROM funcionarios")
            funcionarios = cursor.fetchall()
            id = funcionarios[-1][0]

            # insere dado no banco
            cursor.execute("INSERT INTO funcionarios VALUES(?, ?, ?)", (id+1, nome_usuario, senha_usuario))

            # confirmar a inclusão no banco de dados
            conexao.commit()

            # Label teste cadastro com sucesso
            Ctk.CTkLabel(self, text="Cadastro realizado com sucesso!", fg_color="transparent", text_color="black").pack(pady=10)
   


        def fecha_cadastro_funcionarios():
        
            self.destroy()


        def apagar_textbox_cadastro_usuario(evento):
            textbox_cadastro_usuario.delete("0.0", "end")


        def apagar_textbox_cadastro_senha(evento):
            textbox_cadastro_senha.delete(0, "end")


  

        # Configurações da janela
        self.title("Cadastro funcionários")
        self.geometry("400x500")

        # Caixa de texto nome de usuario
        textbox_cadastro_usuario = Ctk.CTkTextbox(self, width=200, height=20)
        textbox_cadastro_usuario.pack(pady=20)
        textbox_cadastro_usuario.insert("1.0", "Digite seu nome de usuário")
        textbox_cadastro_usuario.bind("<FocusIn>", apagar_textbox_cadastro_usuario)

        # Caixa de texto senha
        textbox_cadastro_senha = Ctk.CTkEntry(self, width=200, height=20, show="*")
        textbox_cadastro_senha.pack(pady=20)
        textbox_cadastro_senha.insert(0, "Digite sua senha")
        textbox_cadastro_senha.bind("<FocusIn>", apagar_textbox_cadastro_senha)
            
        # Botão de confirmação de cadastro
        botao_cadastro = Ctk.CTkButton(self, text="Cadastar", command=cadastro_usuarios)
        botao_cadastro.pack(pady=10)

        # Label link para login
        login_usuario = Ctk.CTkButton(self, text="Já tem uma conta? Faça o login", fg_color="transparent", text_color="black", hover_color="lightgray", command=fecha_cadastro_funcionarios)
        login_usuario.pack(pady=20)

        self.toplevel_window = None

        


class LoginFuncionarios(Ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        def button_callback():
            # Pega todo o texto do textbox
            texto_usuario = textbox_usuario.get("1.0", "end").strip()  
            texto_senha = textbox_senha.get().strip()
            print(texto_usuario)
            print(texto_senha)

            # Label teste login sucesso
            Ctk.CTkLabel(self, text="Login realizado com sucesso!", fg_color="transparent", text_color="black").pack(pady=10)
           


        def apagar_textbox_usuario(evento):
            textbox_usuario.delete("0.0", "end")


        def apagar_textbox_senha(evento):
            textbox_senha.delete("0", "end")



        # Configurações da janela
        self.title("Login funcionários")
        self.geometry("400x320")

        # Caixa de texto nome de usuario
        textbox_usuario = Ctk.CTkTextbox(self, width=200, height=20)
        textbox_usuario.pack(pady=20)
        textbox_usuario.insert("1.0", "Digite seu nome de usuário")
        textbox_usuario.bind("<FocusIn>", apagar_textbox_usuario)

        # Caixa de texto senha
        textbox_senha = Ctk.CTkEntry(self, width=200, height=20, show="*")
        textbox_senha.pack(pady=20)
        textbox_senha.insert(0, "Digite sua senha")
        textbox_senha.bind("<FocusIn>", apagar_textbox_senha)

            
        # Botão de confirmação
        botao_cadastro = Ctk.CTkButton(self, text="Login", command=button_callback)
        botao_cadastro.pack(pady=10)

        # Label link para cadastro
        registro_usuario = Ctk.CTkButton(self, text="Não tem uma conta? Registre-se", fg_color="transparent", text_color="black", hover_color="lightgray", command=self.abre_cadastro_funcionarios)
        registro_usuario.pack(pady=20)

        self.toplevel_window = None


    def abre_cadastro_funcionarios(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CadastroFuncionarios(self)  # create window if its None or destroyed
            self.toplevel_window.attributes("-topmost", True)
            self.toplevel_window.focus_set()
            
        else:
            self.toplevel_window.attributes("-topmost", True) # Garante que a janela fique no topo, se já existir
            self.toplevel_window.focus_set()  # if window exists focus it

    


app = LoginFuncionarios()
app.mainloop()





