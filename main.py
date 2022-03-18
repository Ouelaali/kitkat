from optionT import *



menu_options = {
    1: 'Hash with file',
    2: 'Hash with string',
    3: 'Help',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
    print('Handle option \'Option 1\'')
def option2():
    print('Handle option  \'Option 2\'')
def option3():
    print_menuu()
    new = input("enter your choice")
    


if __name__ == '__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice : '))
        except:
            print('\nWrong input....')
        if option == 1:
            option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('exit')
            exit()
        else: 
             print('\nPlease enter a number between 1 and 4.\n')