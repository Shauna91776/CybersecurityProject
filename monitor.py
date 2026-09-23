import hashlib
import json
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

def save_baseline(baseline, file_path="baseline.json"):
    with open(file_path, "w") as file:
        json.dump(baseline, file, indent=4)


def load_baseline(file_path="baseline.json"):
    with open(file_path, "r") as file:
        return json.load(file)
    
    
def check_integrity(directory, baseline):
    current_files = set()

    for item in directory.iterdir():
        if not item.is_file():
            continue

        current_files.add(item.name)

        current_hash = calculate_hash(item)
        expected_hash = baseline.get(item.name)

        if expected_hash is None:
            print(f"[WARNING] New file detected: {item.name}")
        elif current_hash == expected_hash:
            print(f"[OK] {item.name}")
        else:
            print(f"[WARNING] File modified: {item.name}")

    for filename in baseline:
        if filename not in current_files:
            print(f"[WARNING] File deleted: {filename}")
            


        
    
def main():
    directory = Path("test_files")

    print("========================================")
    print("       FILE INTEGRITY MONITOR")
    print("========================================")
    print()
    print("1. Create baseline")
    print("2. Check integrity")
    print("3. Exit")
    print()

    choice = input("Select an option: ")

    if choice == "1":
        print("Creating baseline...")

        baseline = create_baseline(directory)
        save_baseline(baseline)

        print("Baseline created successfully.")
            

    elif choice == "2":
        print("Checking integrity...")

        baseline = load_baseline()
        check_integrity(directory, baseline)

    elif choice == "3":
        print("Exiting File Integrity Monitor.")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
    
    
                
    

# text = "Hello World"
# #converts text to bytes

# hash_object = hashlib.sha256(text.encode())

# #convert to readable hexaecimal string
# print(hash_object.hexdigest())