import hashlib

# Create an MD5 hash
password = "password123"
hash_object = hashlib.md5(password.encode())
hash_hex = hash_object.hexdigest()

print(hash_hex) 



def process_word(word):

    return f"Processed: {word.upper()}"

def process_wordlist(filepath):

    try:
        with open(filepath, 'r') as file:
            for line in file:

                words = line.strip().split() 
                for word in words:
                    result = process_word(word)
                    print(result)
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
wordlist_file = "wordlist.txt" 
# Create a dummy wordlist file for demonstration
with open(wordlist_file, 'w') as f:
    f.write("wordlist.txt")

process_wordlist(wordlist_file)
