import os
import PySimpleGUI as sg
import string

layout = [
    [sg.Text('Insira o nome do arquivo')],
    [sg.Input(key='arquivo')],
    [sg.Text('Insira o endereço do diretório:')],
    [sg.Input(key='diretorio')],
    [sg.Button('Buscar'),sg.Button('limpar')],
    [sg.Text('',key='mensagem')]
]


def busca(nome_diretorio,nome_arquivo):

    cont = 0

    try:
        for diretorio, subpastas,arquivos in os.walk(nome_diretorio):
            for arquivo in arquivos:
                if nome_arquivo in arquivo:
                    caminho = os.path.join(os.path.realpath(diretorio), arquivo)
                    print(caminho)
                    cont = cont + 1
        if cont == 0:
            print('Arquivo não encontrado')
    except:
        print('erro na busca')



def main():
    window= sg.Window('Busca de arquivos',layout)

    while True:
        event,values=window.read()

        if event == sg.WIN_CLOSED:
            break
        
        elif event == 'Buscar':
            diretorio=values['diretorio']
            arquivo=values['arquivo']
            
            if diretorio == '' or arquivo == '':
                window['mensagem'].update('Nome do arquivo ou nome do diretório faltando')
            else:
                folder = rf"{diretorio}\\"
                busca(folder,arquivo)
        else:
             window['mensagem'].update('')                      
             window['diretorio'].update('')
             window['arquivo'].update('')


main()
