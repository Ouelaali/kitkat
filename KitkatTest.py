import hashlib

# Vérifier et utiliser le type de hash
typeOfHash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_1", "shake_2"]
doneType = True
numberOfType = 0
numberOfTypeOfHash = 0

# Demande du type de hash
while doneType:
    theTypeIsFalse = False
    
    number = int(input("Combien de hash voulez vous : "))
    print("md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512, shake_1, shake_2")
    type = input("Quel type de hash voulez vous (si vous mettez plusieurs hash, séparez les avec des espaces): ")
    # Faire une list de chaque hash
    allType = type.split(" ")
    
    if number == len(allType):
        # Vérifier si les hash sont correct
        while number != numberOfType:
            for j in allType:
                numberOfType += 1
                for i in typeOfHash:
                    if j != i:
                        theTypeIsFalse = True
                    elif j == i:
                        break
    
    if theTypeIsFalse == False:
        doneType = False
    if doneType:
        print("\nCommande incorrect\n")

# Demande de la chaîne de caractere
#message = bytes(input("Veuillez saisir la chaîne de caractère que vous voulez chiffrer : "), encoding="utf_8")
#
#if type == typeOfHash[0]:
#    hash = hashlib.new(typeOfHash[0], message)
#elif type == typeOfHash[1]:
#    hash = hashlib.new(typeOfHash[1], message)
#elif type == typeOfHash[2]:
#    hash = hashlib.new(typeOfHash[2], message)
#elif type == typeOfHash[3]:
#    hash = hashlib.new(typeOfHash[3], message)
#elif type == typeOfHash[4]:
#    hash = hashlib.new(typeOfHash[4], message)
#elif type == typeOfHash[5]:
#    hash = hashlib.new(typeOfHash[5], message)
#elif type == typeOfHash[6]:
#    hash = hashlib.new(typeOfHash[6], message)
#elif type == typeOfHash[7]:
#    hash = hashlib.new(typeOfHash[7], message)
#elif type == typeOfHash[8]:
#    hash = hashlib.new(typeOfHash[8], message)
#elif type == typeOfHash[9]:
#    hash = hashlib.new(typeOfHash[9], message)
#elif type == typeOfHash[10]:
#    hash = hashlib.new(typeOfHash[10], message)
#elif type == typeOfHash[11]:
#    hash = hashlib.new(typeOfHash[11], message)
#elif type == typeOfHash[12]:
#    hash = hashlib.new(typeOfHash[12], message)
#elif type == typeOfHash[13]:
#    hash = hashlib.new(typeOfHash[13], message)
#
#print(hash.hexdigest())