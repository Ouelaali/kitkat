from Hash import Hash

def hashTheFile():
    # 'rb' permet de lire le fichier en binaire 
    # avec f.read() nous pouvons lire et permettre de l'utiliser
    fileToOpen = input("Write the full name of the file to hash (ex: example.txt) : ")
    with open(fileToOpen, 'rb') as f:
        print("\nCAUTION : the file need to be under 65536 bits\n")
        allType = Hash.typeOfHash()
        
        # Put the file in binary
        data = f.read(65536)
        print(data)
        
        Hash.hash(allType, data)