import hashlib
from pathlib import Path


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    hash_object = hashlib.sha256(content)

    return hash_object.hexdigest()


directory = Path("test_files")

for item in directory.iterdir():
    if item.is_file():
        file_hash = calculate_hash(item)
        print(item.name, file_hash)
    

# text = "Hello World"
# #converts text to bytes

# hash_object = hashlib.sha256(text.encode())

# #convert to readable hexaecimal string
# print(hash_object.hexdigest())