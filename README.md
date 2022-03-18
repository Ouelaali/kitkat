# Kitkat :
## Application permit you to hash a string. It's able to code a password with several hash types.

#

## Hash :

## SHA-1
SHA-1 is a popular hash algorithm published in 1994, it was developed by NIST. SHA-1 is similar to the hash algorithms MD4 and MD5, and because it is slightly safer than MD4 and MD5, it is considered the successor of MD5. That said, SHA-1 is also slower than MD5.SHA-1 produces a 160-bit hash. The SHA-1 algorithm is present in a large number of security protocols and applications. Recently Xiaoyun Wang managed to break the popular hashes, proving that SHA-1 was not as safe as it once was considered.
#
## SHA-256
SHA-256 as already mentioned is part of the SHA-2 product family, it is based on SHA-2, but with the capability of larger output strings (up to 256 bits). The design of SHA-256 has changed a bit, however because it is still based on SHA-1 people are skeptical about how safe it is.
#
## SHA-384
SHA-384 is part of the SHA-2 family of algorithms, it is closely based on SHA-1, but the output sizes are increased to 384 bits.
#
## SHA-512
SHA-512 is based on SHA-1 algorithms, however small differences exist. The string is increased in size to 512 bits.
#
## MD5
The MD5, for Message Digest 5, is a cryptographic hash function that allows to obtain the digital footprint of a file. The hash size is 128 bits, and is therefore small enough to allow a birthday attack. The message can contain up to 512 bits.
#
## Blake2b(), Blake2s(): 
BLAKE2 is a set of cryptographic hash functions defined in RFC 7693: The BLAKE2 Cryptographic Hash and Message Authentication Code (MAC). The BLAKE2 family consists of 2 hash functions, and both of them provide security superior to SHA-2. The BLAKE2B is optimized for 64-bit platforms, while the BLAKE2S is optimized for 8-bit to 32-bit platforms. Currently this library supports BLAKE2B algorithm 

#
 The generateBlock module pads the input message and the optional input key into fixed sized blocks, and informs the digest part that how many blocks do we have in this message. The message word size is 64-bit for BLAKE2B, 32-bit for BLAKE2S, and each block has a size of 16 message words.
#
The digest part iteratively computes the hash values. Loop-carried dependency is enforced by the algorithm, and thus this part cannot reach II=1. As these two parts can work independently, they are designed into a parallel dataflow process, connected by streams (FIFOs).
#
A single instance of BLAKE2B function processes input messages at the rate of 1024 bit / 737 cycles at 315.95MHz.
sha3_224, sha3_256, sha3_384, sha3_512: 
SHA-3 comes from the NIST hash function competition which elected the Keccak2 algorithm on October 2, 2012. It is not intended to replace SHA-2, which has not currently been compromised by a significant attack, but to provide another solution following the possibilities of attacks against MD5, SHA-0 and SHA-1 standards.SHA-3 uses sponge construction, in which the input is, metaphorically in a first sentence absorbed by the state, at a certain speed, and in a second squeezed, at the same speed.
To absorb r bits of data, the data is XORée in the first bits of the state, then block permutation is applied if an additional output is desired.
The ability of the hash function, the c=25w-r bits of states that are never directly affected by the input or output, is an important parameter. It can be adjusted according to the expected safety of the construction, but the SHA-3 standard sets it reasonably at c=2n, with n the size of the required footprint.

