import sys
import hashlib

typeOfHash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_1", "shake_2"]
md5 = hashlib.md5()
sha1 = hashlib.sha1()

#Fonction qui permet de hasher dans tous les algorithmes que l'utilisateur a entré
def finalHash(selectedHashes, data):
    for i in selectedHashes:
        if i in typeOfHash:
            print(i + " :  {0}".format(hashlib.new(i, data).hexdigest()))

# 'rb' permet de lire le fichier en binaire 
# avec f.read() nous pouvons lire et permettre de l'utiliser
with open(sys.argv[1], 'rb') as f:
    
    selectedHashes = input('Avec quel algorithme de hash parmis ceux du dessous vouslez-vous hasher le fichier ?')
    while True:
        data = f.read(65536)
        # print(data)
        if not data:
            break
        finalHash(selectedHashes, data)
