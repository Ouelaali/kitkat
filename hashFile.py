import sys
import hashlib

md5 = hashlib.md5()
sha1 = hashlib.sha1()

# 'rb' permet de lire le fichier en binaire 
# avec f.read() nous pouvons lire et permettre de l'utiliser
with open(sys.argv[1], 'rb') as f:
    while True:
        data = f.read(65536)
        print(data)
        if not data:
            break
        md5.update(data)
        sha1.update(data)

print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))