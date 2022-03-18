import sys
from Hash import Hash

def hashTheFile():
    # 'rb' permet de lire le fichier en binaire 
    # avec f.read() nous pouvons lire et permettre de l'utiliser
    with open(sys.argv[1], 'rb') as f:
        print("\nCAUTION : the file need to be under 65536 bits\n")
        allType = Hash.typeOfHash()
        
        # Put the file in binary
        data = f.read(65536)
        print(data)
        
        Hash.hash(allType, data)