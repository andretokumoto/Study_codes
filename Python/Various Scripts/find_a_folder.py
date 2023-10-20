
# Program that scans folders and subfolders from a root directory
# and returns the address of the searched folder

# Application screen layout
layout = [
    [sg.Text('Enter the folder name')],
    [sg.Input(key='folder')],
    [sg.Text('Enter the directory name:')],
    [sg.Input(key='directory')],
    [sg.Button('Search'), sg.Button('Clear')],
    [sg.Text('', key='message')]
]

# This function scans the folders from the directory and returns the desired folder's path
def search(directory_name, folder_name):

    count = 0

    try:
        for directory, subfolders, files in os.walk(directory_name):
            for folders in subfolders:
                if folders == folder_name:
                    path = os.path.realpath(directory)
                    print(path)
                    count = count + 1
        if count == 0:
            print('Folder not found')
    except:
        print('Search error')

def main():
    window = sg.Window('Directory Comparator', layout)

    # Definition of screen events and data requests
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

        elif event == 'Search':
            directory = values['directory']
            folder = values['folder']

            if directory == '' or folder == '':
                window['message'].update('Folder name or directory name missing')
            else:
                folder_path = rf"{directory}\\"
                search(folder_path, folder)
        else:
            window['message'].update('')
            window['directory'].update('')
            window['folder'].update('')

main()
