from Hash import Hash

def hashTheString():
    allType = Hash.typeOfHash()

    # Ask the string
    message = bytes(input("Please enter the string you want to encrypt : "), encoding="utf_8")

    # Hash
    Hash.hash(allType, message)