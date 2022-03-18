from hashString import hashTheString
from hashFile import hashTheFile
from help import helpHash

menu_options = {
    1: 'Hash with file',
    2: 'Hash with string',
    3: 'Help',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def mainMenu():
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice : '))
        except:
            print('\nWrong input....')
        if option == 1:
            hashTheFile()
        elif option == 2:
            hashTheString()
        elif option == 3:
            helpHash()
        elif option == 4:
            print('exit')
            exit()
        else: 
             print('\nPlease enter a number between 1 and 4.\n')

if __name__ == '__main__':
    mainMenu()