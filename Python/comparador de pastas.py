import os
import PySimpleGUI as sg
import string


layout = [
    [sg.Text('Insira o endereço do 1° diretório:')],
    [sg.Input(key='diretorio1')],
    [sg.Text('Insira o endereço do 2° diretório:')],
    [sg.Input(key='diretorio2')],
    [sg.Button('COMPARAR')],
    [sg.Text('',key='mensagem'),sg.Button('limpar')],
]


def compara_dir(folder1,folder2):

    cont = 0
    try:
        print('arquivos no diretório 2 que não estão presentes no diretório 1:\n')
        for diretorio, subpastas, arquivos in os.walk(folder1):
            for diretorio2, subpastas2, arquivos2 in os.walk(folder2):
                for arquivo in arquivos2:
                    if arquivo not in arquivos:
                        cont = cont + 1
                        caminho = os.path.join(os.path.realpath(diretorio2), arquivo)
                        print('arquivo :'+caminho)
                        
        print('\n\narquivos no diretório 1 que não estão presentes no diretório 2:\n')                
        for diretorio, subpastas, arquivos in os.walk(folder2):
            for diretorio2, subpastas2, arquivos2 in os.walk(folder1):
                for arquivo in arquivos2:
                    if arquivo not in arquivos:
                        cont = cont + 1
                        caminho = os.path.join(os.path.realpath(diretorio2), arquivo)
                        print('arquivo :'+caminho)
        if cont == 0:
            print("Os diretórios são iguais")
    except:
        print('Falha na comparação')

def main():
    window= sg.Window('Comparador de diretórios',layout)

    while True:
        event,values=window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == 'COMPARAR':
            diretorio1=values['diretorio1']
            diretorio2=values['diretorio2']
            if diretorio1 == '' or diretorio2 == '':
                window['mensagem'].update('digite os dois diretórios para comparação')
            else:
                folder1 = rf"{diretorio1}\\"
                folder2 = rf"{diretorio2}\\"
                compara_dir(folder1,folder2)
        else:
             window['mensagem'].update('')                      
             window['diretorio1'].update('')
             window['diretorio2'].update('')
main()
