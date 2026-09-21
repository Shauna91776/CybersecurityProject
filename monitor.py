import hashlib

text = "Hello World"
#converts text to bytes

hash_object = hashlib.sha256(text.encode())

#convert to readable hexaecimal string
print(hash_object.hexdigest())