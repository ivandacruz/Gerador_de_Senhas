import random
import PySimpleGUI as sg
import os
from playsound import playsound

class PassGen:
    def __init__(self):
        # layout
        sg.theme('Black')
        playsound('secret.mp3', block=false )
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
            sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)),
            sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]
    # Declarando Janela
        self.janela = sg.Window('Password Generator', layout)
    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)

    def gerar_senha(self, valores):
        char_list ='ABCÇDEFGHIJKLMNOPQRSTUVWXYZabcçddefghijklmnopqrstuvwxyz123456789!@$%¨&*'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        new_pass = ''.join(chars)
        return new_pass


    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a') as file:
            file.write(f"{valores['site']}{valores['usuario']}{os.linesep}")
        print('Senha salva para o arquivo "Senhas.txt"')

gen = PassGen()
gen.Iniciar()    