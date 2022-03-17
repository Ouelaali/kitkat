import hashlib

class Hash:
    def hash(allType, message):
        for j in allType:
            hash = hashlib.new(j, message)
            message = bytes(hash.hexdigest(), encoding="utf_8")

        print(hash.hexdigest())