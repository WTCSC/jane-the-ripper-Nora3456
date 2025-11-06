import hashlib

password = "password123" # Replace "password123" with the word you would like to hash.
hash_object = hashlib.md5(password.encode())
hash_hex = hash_object.hexdigest()

print(hash_hex)  # This line gives you your hashed password. In the case of the word "password123", 
#                  the output is: 482c811da5d5b4bc6d497ffa98491e38