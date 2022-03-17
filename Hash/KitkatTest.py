from Hash import hash

allType = hash.typeOfHash()

# Ask the string
message = bytes(input("Please enter the string you want to encrypt : "), encoding="utf_8")

# Hash
hash.hash(allType, message)