


import customtkinter as Ctk



class ToplevelWindow(Ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def cadastro_usuarios():
            # Pega todo o texto do textbox
            texto_cadastro_usuario = textbox__cadastro_usuario.get("1.0", "end").strip()  
            texto_cadastro_senha = textbox_cadastro_senha.get("1.0", "end").strip()
            print(f"Funcionário {texto_cadastro_usuario} cadastrado com sucesso")
            print(texto_cadastro_usuario)


        # def apagar_textbox_cadastro_usuario(evento):
        #     texto_cadastro_usuario.delete("0.0", "end")


        # def apagar_textbox_cadastro_senha(evento):
        #     texto_cadastro_senha.delete("0.0", "end")



        # Configurações da janela
        self.title("Cadastro funcionários")
        self.geometry("500x600")

        # Caixa de texto nome de usuario
        textbox__cadastro_usuario = Ctk.CTkTextbox(self, width=200, height=20)
        textbox__cadastro_usuario.pack(pady=20)
        textbox__cadastro_usuario.insert("1.0", "Digite seu nome de usuário")
        #textbox__cadastro_usuario.bind("<FocusIn>", apagar_textbox_cadastro_usuario)

        # Caixa de texto senha
        textbox_cadastro_senha = Ctk.CTkTextbox(self, width=200, height=20)
        textbox_cadastro_senha.pack(pady=20)
        textbox_cadastro_senha.insert("1.0", "Digite sua senha")
        #textbox_cadastro_senha.bind("<FocusIn>", apagar_textbox_cadastro_senha)

            
        # Botão de confirmação de cadastro
        botao_cadastro = Ctk.CTkButton(self, text="Cadastar", command=cadastro_usuarios)
        botao_cadastro.pack(pady=10)

        self.toplevel_window = None


class Login(Ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        def button_callback():
            # Pega todo o texto do textbox
            texto_usuario = textbox_usuario.get("1.0", "end").strip()  
            texto_senha = textbox_senha.get("1.0", "end").strip()
            print(texto_usuario)
            print(texto_senha)


        def apagar_textbox_usuario(evento):
            textbox_usuario.delete("0.0", "end")


        def apagar_textbox_senha(evento):
            textbox_senha.delete("0.0", "end")



        # Configurações da janela
        self.title("Login funcionários")
        self.geometry("400x250")

        # Caixa de texto nome de usuario
        textbox_usuario = Ctk.CTkTextbox(self, width=200, height=20)
        textbox_usuario.pack(pady=20)
        textbox_usuario.insert("1.0", "Digite seu nome de usuário")
        textbox_usuario.bind("<FocusIn>", apagar_textbox_usuario)

        # Caixa de texto senha
        textbox_senha = Ctk.CTkTextbox(self, width=200, height=20)
        textbox_senha.pack(pady=20)
        textbox_senha.insert("1.0", "Digite sua senha")
        textbox_senha.bind("<FocusIn>", apagar_textbox_senha)

            
        # Botão de confirmação
        botao_cadastro = Ctk.CTkButton(self, text="Login", command=button_callback)
        botao_cadastro.pack(pady=10)

        registro_usuario = Ctk.CTkButton(self, text="Não tem uma conta? Registre-se", fg_color="transparent", text_color="black", command=self.open_toplevel)
        registro_usuario.pack(pady=20)

        self.toplevel_window = None


    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it


app = Login()
app.mainloop()