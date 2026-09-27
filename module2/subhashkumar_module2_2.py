# # subhashkumar_module2_2.py

# # make python function code to encrypt a string. 
# # Make your own encryption method and explain it.   


import random
import string

# cypher encryption program, 
# basicaly created a radom shifted keys for all possible chars
# encrypt and decrypt share the keys only if it is same instance

class CypherEncryption:
    """Prepare a custom enryption logic."""
    possible_chars = " " + string.punctuation + string.digits + string.ascii_letters
    local_random = random.Random()  # 42 is the seed
    

    def __init__(self):
        self.chars = list(CypherEncryption.possible_chars)
        

    #ENCRYPT
    def encrypt(self,plain_text):
        self.key = self.chars.copy()
        CypherEncryption.local_random.shuffle(self.key)
        
        #plain_text = input("Enter a message to encrypt: ")
        cipher_text = ""

        for letter in plain_text:
            index = self.chars.index(letter)
            cipher_text += self.key[index]

        # Return the complete encrypted string.
        return cipher_text

    #DECRYPT
    def decrypt(self, cipher_text, enc_key):
        #cipher_text = input("Enter a message to decrypt: ")
        plain_text = ""

        #self.key = enc_key.split(",")
        

        # replace each character position by the key index.
        for letter in cipher_text:
            index = self.key.index(letter)
            plain_text += self.chars[index]

        # Return the complete decrypted string.
        return plain_text



# Test Encryption
# Get text from the user.
plain_text = input("Enter a string to encrypt: ")

# Encrypt the input string.
enc = CypherEncryption()
cipher_text = enc.encrypt(plain_text)

# Display original string
print(f"original message : {plain_text}")
# Display the encrypted string.
print(f"encrypted message: {cipher_text}")
enc_key = ",".join(enc.key)
#print(f"encryption key: {enc_key}")


# Test Decryption
# Get Encrypted text from the user.
cipher_text = input("Enter a Encrypted string: ")

# Decrypt the input string.
dec = CypherEncryption()
plain_text = enc.decrypt(cipher_text, enc_key)

# Display the encrypted string.
print(f"encrypted message: {cipher_text}")
# Display original string
print(f"original message : {plain_text}")
#enc_key = ",".join(dec.key)
##print(f"encryption key: {enc_key}")





