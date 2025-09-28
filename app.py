import customtkinter as ctk


#criaçao das funçoes de funcionalidade
def validarLogin():
    usuario = campoUsuario.get()
    senha = campoSenha.get()
    if usuario == 'kluivert' and senha == '895623':
        resultado.configure(text='Login feito co sucesso', text_color='green')
    else:
        resultado.configure(text='Usuario ou senha incorretos',text_color='red')
#configurar aparencia
ctk.set_appearance_mode('dark')

#criaçao da janela de aparencia
app = ctk.CTk()
app.title('Sistema de login')
app.geometry('300x300')
#criaçao dos campos
#label
LabelUsuario = ctk.CTkLabel(app, text='Usuário')
LabelUsuario.pack(pady=10)
#entry
campoUsuario = ctk.CTkEntry(app, placeholder_text='Digite o usuario: ')
campoUsuario.pack(pady=10)
#label
LabelSenha = ctk.CTkLabel(app, text='Senha')
LabelSenha.pack(pady=10)
#entry
campoSenha = ctk.CTkEntry(app, placeholder_text='Digite sua senha: ', show='*')
campoSenha.pack(pady=10)
#bottom
campoBotao = ctk.CTkButton(app, text='Login', command=validarLogin)
campoBotao.pack(pady=10)
#feedback de login
resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady=10)
#iniciar aplicaçao
app.mainloop()