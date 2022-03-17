
from ast import Return


menuu_options =  {
    1: 'Help Hash',
    2: 'Help',
    3: 'return'
}

def print_menuu():
    for key in menuu_options.keys():
        print (key, '--', menuu_options[key] )

def option1():
    print('Handle option \'Option 1\'')

def option2():
    print('Handle option \'Option 2\'')

def option3():
    print('Handle option \'Option 3 \'')

class test:
    if __name__ == '__main__':
        while(True):
            print_menuu()
            option = '3'
            try:
                option = int(input('Enter your choice :  '))
            except:
                print('\nWrong input. Please enter a number ...\n')
            if option == 1:
                option1()
            elif option == 2:
                option2()
            elif option == 3:
                print('return')
                Return
            else: 
                print('\nInvalid option. Please enter a number between 1 and 2\n')

