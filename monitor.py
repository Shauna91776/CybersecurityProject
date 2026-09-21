import hashlib
from pathlib import Path


def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()

    hash_object = hashlib.sha256(content)

    return hash_object.hexdigest()


def create_baseline(directory):
    baseline = {}

    for item in directory.iterdir():
        if not item.is_file():
            continue

        file_hash = calculate_hash(item)
        baseline[item.name] = file_hash

    return baseline


directory = Path("test_files")

baseline = create_baseline(directory)

print(baseline)
                
    

# text = "Hello World"
# #converts text to bytes

# hash_object = hashlib.sha256(text.encode())

# #convert to readable hexaecimal string
# print(hash_object.hexdigest())