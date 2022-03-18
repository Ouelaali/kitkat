from hashString import hashTheString
from hashFile import hashTheFile

menu_options = {
    1: 'Hash with file',
    2: 'Hash with string',
    3: 'Help',
    4: 'Exit',
}

menuu_options =  {
    1: 'Help Hash',
    2: 'Help',
    3: 'return'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    hashTheFile()
def option2():
    hashTheString()
def option3():
    print_menuu()
    new = input("Enter your choice : ")
    

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
            helpMenu()
        elif option == 4:
            print('exit')
            exit()
        else: 
             print('\nPlease enter a number between 1 and 4.\n')

def helpMenu():
    while(True):
        print_menuu()
        option = ''
        try:
            option = int(input('Enter your choice :  '))
        except:
            print('\nWrong input. Please enter a number ...\n')
        if option == 1:
            print('Handle option \'Option 1\'')
        elif option == 2:
            print('Handle option \'Option 2\'')
        elif option == 3:
            print('return')
            mainMenu()
            exit()
        else: 
            print('\nInvalid option. Please enter a number between 1 and 2\n')


if __name__ == '__main__':
    mainMenu()