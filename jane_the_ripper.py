"""
File: jane_the_ripper.py
Author: Nora Rice
Date Created: 2025-11-01
Date Last Modified: 2025-11-07
Description: This script runs a code that cracks passwords, by obtaining a hashed passwords file, and wordlist file. Using the two files, it MD5 hashes the wordlist file, and checks to see if that hasshes wordlist files matches any lines in the hash file, thus, cracking passwords!
"""

import hashlib
import os
from collections import defaultdict

# Stores hashes lines in wordlist file
hash_to_passwords = defaultdict(list)


def process_wordlist(filename):
    """
    Reads the wordlist file one line at a time, then hashes each line and stores it in "hash_to_passwords."
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                password = line.strip() 
                if not password:
                    continue
                hash_hex = hashlib.md5(password.encode('utf-8')).hexdigest()
                hash_to_passwords[hash_hex].append(password)
    except Exception as e:
        print("Error processing wordlist:", e)


def check_matching_words(filename):
    """
    Reads the targer hash file, and checks ti see if the the target hash exists in the 'hash_to_passwords."
    """
    found_any = False
    try:
        with open(filename, 'r') as file: 
            for line in file:
                target = line.strip()
                if not target:
                    continue
                if target in hash_to_passwords:
                    found_any = True
                    for password in hash_to_passwords[target]:
                        print(f"Password Cracked!: {target} ----> {password}")
                else:
                    print(f"Unable to crack the password for: {target}")
        if not found_any:
            print("No passwords cracked.")
    except Exception as e:
        print("Error checking hashes:", e)


def ask_file_path(prompt):
    """
    Asks the user for input; the path to the hash file, and then path to the wordlist file. The imputs run in a loop, and break once the user gives an existing files name. 
    """
    while True:
        path = input(prompt).strip()
        if os.path.isfile(path):
            return path
        print(f"File not found: {path}")


if __name__ == "__main__":
    print("Hello, welcome to Jane the Ripper, otherwise known as the password cracker!")


    path_to_hashes = ask_file_path("Enter path to hash file: ")

    path_to_wordlist = ask_file_path("Enter path to wordlist file: ")

    # Sets each function with the paramters, using input from the users wordlist and hash file
    process_wordlist(path_to_wordlist)
    check_matching_words(path_to_hashes)


