import sys
import hashlib
from Hash import Hash

typeOfHash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_1", "shake_2"]

#Fonction qui permet de hasher dans tous les algorithmes que l'utilisateur a entré
# def finalHash(allType, data):
#     for i in allType:
#         if i in typeOfHash:
#             print(i + " :  {0}".format(hashlib.new(i, data).hexdigest()))
#             data = bytes(hashlib.new(i, data).hexdigest(), encoding="utf_8")
            

# 'rb' permet de lire le fichier en binaire 
# avec f.read() nous pouvons lire et permettre de l'utiliser
with open(sys.argv[1], 'rb') as f:
    print(*typeOfHash)
    selectedHashes = input('Choose the type on hash to use on the file (if you put several hashes, separate them with spaces): ')
    allType = selectedHashes.split(" ")
    while True:
        data = f.read(65536)
        if not data:
            print('This file is too heavy to be hashed')
            break
        Hash.hash(allType, data)
        # finalHash(allType, data)

