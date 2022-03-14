import hashlib

# Type de hash
h = hashlib.new('sha256')
# Message a hasher
h.update(b"message")
# Affichage
print(h.hexdigest())