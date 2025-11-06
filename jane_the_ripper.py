import hashlib
import os
from collections import defaultdict


hash_to_passwords = defaultdict(list)


def process_wordlist(filename):
    """Populate hash_to_passwords with md5(password) -> [password,...]."""
    try:
        with open(filename, 'r') as file: #encoding='utf-8', errors='ignore') as fh:
            for line in file:
                password = line.strip() # rstrip('\n')
                if not password:
                    continue
                hash_hex = hashlib.md5(password.encode('utf-8')).hexdigest()
                hash_to_passwords[hash_hex].append(password)
    except Exception as e:
        print("Error processing wordlist:", e)


def check_matching_words(filename):
    """Read file of hashes (one per line). Print matches and corresponding plaintext(s)."""
    found_any = False
    try:
        with open(filename, 'r') as file: # encoding='utf-8', errors='ignore') as fh:
            for line in file:
                target = line.strip()
                if not target:
                    continue
                if target in hash_to_passwords:
                    found_any = True
                    # There may be multiple plaintexts for a single hash (rare), print them all
                    for password in hash_to_passwords[target]:
                        print(f"Password Cracked!: {target} ----> {password}")
                else:
                    print(f"Unable to crack the password for: {target}")
        if not found_any:
            print("No passwords cracked.")
    except Exception as e:
        print("Error checking hashes:", e)


def ask_file_path(prompt):
    while True:
        path = input(prompt).strip()
        if os.path.isfile(path):
            return path
        print(f"File not found: {path}")


if __name__ == "__main__":
    print("Hello, welcome to Jane the Ripper, otherwise known as the password cracker!")


    path_to_hashes = ask_file_path("Enter path to hash file: ")

    path_to_wordlist = ask_file_path("Enter path to wordlist file: ")

    process_wordlist(path_to_wordlist)
    check_matching_words(path_to_hashes)


