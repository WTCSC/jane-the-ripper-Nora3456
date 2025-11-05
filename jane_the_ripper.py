import hashlib
clean_words = set()


def process_wordlist(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                password = line.strip()
                hash_object = hashlib.md5(password.encode())
                hash_hex = hash_object.hexdigest()
                clean_words.add(hash_hex)     
    except ValueError:
        print("error")


def check_matching_words(filename):
    found = False
    try:
        with open(filename, 'r') as file:
            for line in file:
                hash_line = line.strip()
                if hash_line in clean_words:
                    print(f"Match found: {hash_line}")
                    found = True
                if not found:
                    print("No matches found.")
    except Exception as e:
        print("Error checking hashes:", 'e')

"""def check_matching_words(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                processed_line_file = line.strip().lower()
                if processed_line_file in clean_words:
                    print(f"Match found: {process_wordlist(filename)} = {processed_line_file}")
                    found = True
    except ValueError:
        print("error")"""

                
import os

# Verifies that the file the user input for their hash file exists
while True:
    try: 
        path_to_hash = input("Enter path to hash file: ")
        if os.path.isfile(path_to_hash):
            break
        else:
            print(f"The file '{path_to_hash}' does not exist, try again.")
    except ValueError:
        print("error")

# Verifies that the file the user input for their wordlist file exists
while True:
    try:
        path_to_wordlist = input("Enter path to wordlist file: ")

        if os.path.isfile(path_to_wordlist):
            break
        else:
            print(f"The file '{path_to_wordlist}' does not exist, try again.")
    except ValueError:
        print("error")

check_matching_words(path_to_hash)
process_wordlist(path_to_wordlist)