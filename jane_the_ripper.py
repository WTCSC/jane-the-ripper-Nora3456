import hashlib
clean_words = set()

def process_wordlist(path_to_hash):
    try:
        with open(path_to_hash, 'r') as file:
            for line in file:
                password = line.strip()
                hash_object = hashlib.md5(password.encode())
                hash_hex = hash_object.hexdigest()
                return hash_hex     
    except ValueError:
        print("error")

def check_matching_words(path_to_wordlist                                                                                                                                                           ):
        with open(path_to_wordlist, 'r') as file2:
            for line in file2:
                processed_line_f2 = line.file2.strip().lower()
                if processed_line_f2 in process_wordlist.file:
                    print(f"Match found: '{processed_line_f2}'")
                    return True  # A match was found
        return False  # No matches found


                
import os
while True:
    try: 
        path_to_hash = input("Enter path to hash file: ")
        if os.path.isfile(path_to_hash):
            break
        else:
            print(f"The file '{path_to_hash}' does not exist, try again.")
    except ValueError:
        print("error")

while True:
    try:
        path_to_wordlist = input("Enter path to wordlist file: ")

        if os.path.isfile(path_to_wordlist):
            break
        else:
            print(f"The file '{path_to_wordlist}' does not exist, try again.")
    except ValueError:
        print("error")

print(f"{check_matching_words()}")

