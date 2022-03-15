import hashlib

# Vérifier et utiliser le type de hash
typeOfHash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_1", "shake_2"]
doneType = True

# Demande du type de hash
while doneType:
    print("md5, sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512, shake_1, shake_2")
    type = input("Quel type de hash voulez vous : ")
    for i in typeOfHash:
        if type == i:
            doneType = False
    if doneType:
        print("\nCommend incorrect\n")

# Demande de la chaîne de caractere
message = bytes(input("Quel est votre message : "), encoding="utf_8")

if type == typeOfHash[0]:
    hash = hashlib.new(typeOfHash[0], message)
elif type == typeOfHash[1]:
    hash = hashlib.new(typeOfHash[1], message)
elif type == typeOfHash[2]:
    hash = hashlib.new(typeOfHash[2], message)
elif type == typeOfHash[3]:
    hash = hashlib.new(typeOfHash[3], message)
elif type == typeOfHash[4]:
    hash = hashlib.new(typeOfHash[4], message)
elif type == typeOfHash[5]:
    hash = hashlib.new(typeOfHash[5], message)
elif type == typeOfHash[6]:
    hash = hashlib.new(typeOfHash[6], message)
elif type == typeOfHash[7]:
    hash = hashlib.new(typeOfHash[7], message)
elif type == typeOfHash[8]:
    hash = hashlib.new(typeOfHash[8], message)
elif type == typeOfHash[9]:
    hash = hashlib.new(typeOfHash[9], message)
elif type == typeOfHash[10]:
    hash = hashlib.new(typeOfHash[10], message)
elif type == typeOfHash[11]:
    hash = hashlib.new(typeOfHash[11], message)
elif type == typeOfHash[12]:
    hash = hashlib.new(typeOfHash[12], message)
elif type == typeOfHash[13]:
    hash = hashlib.new(typeOfHash[13], message)

print(hash.hexdigest())