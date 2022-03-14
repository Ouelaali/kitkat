import hashlib

h = hashlib.new('sha256')
h.update(b"message")
print(h.hexdigest())