import hashlib

# Example 1
# Type de hash
h = hashlib.new('sha256')
# Message a hasher
h.update(b"message")
# Affichage
print(h.hexdigest())

# Example 2
myMessage = b"it's my message"
h = hashlib.new('md5', myMessage)
print(h.hexdigest())