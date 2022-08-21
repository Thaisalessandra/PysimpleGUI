import PySimpleGUI as sg


class TeladoPrograma :
    pass


class TeladoPrograma:
    def __init__(self):
        #layout-- aqui é a cara do programa e onde os dados serão pegos pelo programa
        layout=[[sg.Text('Nome:',size=(5,0)),sg.Input(key='nome')],
                [sg.Text('Idade:',size=(5,0)),sg.Input(key='idade')],
                [sg.Text("Quais provedores de email você possui")],
                [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook')],
                [sg.Button("Enviar Dados")],
                 ]
        #janela
        janela = sg.Window('Dados do usuário').layout(layout)
        #Extrair dados da tela -- Aqui os dados são extraidos para as variaveis para que o dado possa ser manipulado
        self.button,self.values=janela.Read()
    def Iniciar(self):
        nome = self.values['nome']
        idade= self.values['idade']
        aceita_gmail=self.values['gmail']
        aceita_outlook = self.values['outlook']
        #O print foi utilizado apenas para ver se os dados estão sendo pegos de forma correta
        print(f'nome:{nome}')
        print(f'Idade:{idade}')
        print(f'Aceita Gmail:{aceita_gmail}')
        print((f'Aceita Outlook:{aceita_outlook}'))

tela =TeladoPrograma()
tela.Iniciar()
