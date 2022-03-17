#from hashlib import md5
from select import select
from tabulate import tabulate

print(" \nVoici la liste des différents HASH() ")
print()

print(tabulate([["NUMEROS","HASH"],
[  ],
[1,"SHA-1"],
[2,"SHA-256"],
[3,"SHA-384"],
[4,"SHA-512"],
[5,"MD5"],
[6,"BLAKE2B(), BLAKE2S()"],
[7,"SHA3_224, SHA3_256, SHA3_384, SHA3_512"]],
tablefmt="rst"))



def switch():
    option = int(input("entrer le numero du hash : "))

    if option == 1:
        result = "SHA-1 is a popular hash algorithm published in 1994, it was developed by NIST. SHA-1 is similar to the hash algorithms MD4 and MD5, and because it is slightly safer than MD4 and MD5, it is considered the successor of MD5. That said, SHA-1 is also slower than MD5.SHA-1 produces a 160-bit hash. The SHA-1 algorithm is present in a large number of security protocols and applications. Recently Xiaoyun Wang managed to break the popular hashes, proving that SHA-1 was not as safe as it once was considered."
        print(result)

 
    elif option == 2:
        result =  "SHA-256 as already mentioned is part of the SHA-2 product family, it is based on SHA-2, but with the capability of larger output strings (up to 256 bits). The design of SHA-256 has changed a bit, however because it is still based on SHA-1 people are skeptical about how safe it is."
        print(result)
 
    elif option == 3:
        result = "SHA-384 is part of the SHA-2 family of algorithms, it is closely based on SHA-1, but the output sizes are increased to 384 bits."
        print(result)

    elif option == 4:
        result = "SHA-512 is based on SHA-1 algorithms, however small differences exist. The string is increased in size to 512 bits."
        print(result)

    elif option == 5:
        result = "The MD5, for Message Digest 5, is a cryptographic hash function that allows to obtain the digital footprint of a file. The hash size is 128 bits, and is therefore small enough to allow a birthday attack. The message can contain up to 512 bits."
        print(result)

    elif option == 6:
        result = " BLAKE2 is a set of cryptographic hash functions defined in RFC 7693: The BLAKE2 Cryptographic Hash and Message Authentication Code (MAC). \n The BLAKE2 family consists of 2 hash functions, and both of them provide security superior to SHA-2. \nThe BLAKE2B is optimized for 64-bit platforms, while the BLAKE2S is optimized for 8-bit to 32-bit platforms. Currently this library supports BLAKE2B algorithm \n The generateBlock module pads the input message and the optional input key into fixed sized blocks, and informs the digest part that how many blocks do we have in this message. \nThe message word size is 64-bit for BLAKE2B, 32-bit for BLAKE2S, and each block has a size of 16 message words.\nThe digest part iteratively computes the hash values. Loop-carried dependency is enforced by the algorithm, and thus this part cannot reach II=1. \nAs these two parts can work independently, they are designed into a parallel dataflow process, connected by streams (FIFOs).\nA single instance of BLAKE2B function processes input messages at the rate of 1024 bit / 737 cycles at 315.95MHz."
        print(result)

    elif option == 7:
        result = "SHA-3 comes from the NIST hash function competition which elected the Keccak2 algorithm on October 2, 2012. It is not intended to replace SHA-2, which has not currently been compromised by a significant attack, but to provide another solution following the possibilities of attacks against MD5, SHA-0 and SHA-1 standards.SHA-3 uses sponge construction, in which the input is, metaphorically in a first sentence absorbed by the state, at a certain speed, and in a second squeezed, at the same speed.\nTo absorb r bits of data, the data is XORée in the first bits of the state, then block permutation is applied if an additional output is desired.\nThe ability of the hash function, the c=25w-r bits of states that are never directly affected by the input or output, is an important parameter. It can be adjusted according to the expected safety of the construction, but the SHA-3 standard sets it reasonably at c=2n, with n the size of the required footprint."
        print(result)
 
    else:
        print("Incorrect option")
 
 
 
switch()