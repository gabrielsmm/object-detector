import PySimpleGUI as sg
import deteccao

class TelaPython:
    def __init__(self):
        #Layout
        self.image_elem = sg.Image(filename='', key="imagem")
        sg.theme('DarkBlue1')

        col = sg.Col( [[self.image_elem]], size=(500,500), pad=(0,0))

        layout = [
            [sg.Text('Selecione o arquivo que deseja detectar')],
            [sg.Button('Carregar arquivo')],
            [sg.Text('Selecione a forma de detecção que deseja utilizar')],
            [sg.Button('Detectar imagem'), sg.Button('Detectar vídeo')]
        ]
        #Janela
        self.janela = sg.Window("Detector de objetos em imagens e vídeos").layout(layout)
        
    def Iniciar(self):
        detect = deteccao.Deteccao()
        while True:
            event, values = self.janela.read()
            
            if event == 'Carregar arquivo':
                filename = sg.popup_get_file('Entre com o arquivo que deseja detectar')
                print(filename)
            elif event == 'Detectar imagem':
                detect.detectar_imagem(filename)
            elif event == 'Detectar vídeo':
                detect.detectar_video(filename)
            elif event == sg.WINDOW_CLOSED:
                break

tela = TelaPython()
tela.Iniciar()