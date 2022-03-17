import hashlib

class Hash:
    def hash(allType, message):
        for j in allType:
            hash = hashlib.new(j, message)
            message = bytes(hash.hexdigest(), encoding="utf_8")

        print(hash.hexdigest())
    
    def typeOfHash():
        # Ask the type of hash
        typeOfHash = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_1", "shake_2"]
        # theTypeIsFalse = False
        doneType = True
        numberOfType = 0
        foundCount = 0
        while doneType:
            
            number = int(input("How many hashes do you want : "))
            print("md5, sha1, sha224, sha256, sha384, sha512 (recommended), blake2b, blake2s, sha3_224, sha3_256, sha3_384, sha3_512, shake_1, shake_2")
            type = input("What type of hash do you want (if you put several hashes, separate them with spaces) : ")
            # Do a list of hash
            allType = type.split(" ")
            
            if number == len(allType):
                # Verify the hash
                while number != numberOfType:
                    for j in allType:
                        foundTheHash = False
                        numberOfType += 1
                        for i in typeOfHash:
                            if j == i:
                                foundTheHash = True
                                if foundTheHash:
                                    foundCount += 1
                                break
            
            if number == foundCount:
                doneType = False
            if doneType:
                print("\nIncorrect order\n")
        return allType