# Program that changes all files of a specific extension to another desired extension

import os
import PySimpleGUI as sg
import string

layout = [
    [sg.Text('Enter the folder address (directory) you desire:')],
    [sg.Input(key='directory')],
    [sg.Text('Change files with extension: '), sg.Input(key='extensionStart')],
    [sg.Text('To extension: '), sg.Input(key='extensionEnd')],
    [sg.Button('CONVERT')],
    [sg.Text('', key='message'), sg.Button('clear')],
]

def change_extension(initialExtension, finalExtension, directory):

    extLength = len(initialExtension)
    try:
        for file_name in os.listdir(directory):

            nameLength = len(file_name)
            newLength = nameLength - extLength
            term = file_name[newLength:nameLength]

            if initialExtension == term:

                old_name = directory + '\\' + file_name
                new_name = directory + '\\' + file_name[0:newLength] + finalExtension
                os.rename(old_name, new_name)

        message_return = 'Data converted successfully!'
        return message_return

    except:
        message_return = 'Conversion error'
        return message_return

def main():
    window = sg.Window('Extension Converter', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        elif event == 'CONVERT':
            directory = values['directory']
            folder = rf"{directory}\\"
            extStart = values['extensionStart']
            extEnd = values['extensionEnd']

            if directory == '':
                window['message'].update('Enter a directory')
            elif extStart == '':
                window['message'].update('Enter a valid initial extension')
            elif extEnd == '':
                window['message'].update('Enter a valid final extension')
            else:
                conv = change_extension(extStart, extEnd, directory)
                window['message'].update(conv)
                window['directory'].update('')
                window['extensionStart'].update('')
                window['extensionEnd'].update('')

        elif event == 'clear':
            window['message'].update('')
            window['directory'].update('')
            window['extensionStart'].update('')
            window['extensionEnd'].update('')

main()
