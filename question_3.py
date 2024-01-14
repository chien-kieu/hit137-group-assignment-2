
"""
QUESTION 3

Link to git: https://github.com/chien-kieu/hit137-group-assignment-2/blob/main/question_3.py
"""
def finding_decryption_key():
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= i - j

    counter = 0
    while counter < 5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2
    return total

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text +=chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Read encrypted content from a text file
encrypted_file_path = 'encrypted_code.text'
with open(encrypted_file_path, 'r') as file:
    encrypted_content = file.read()
    print('Encrypted_content: \n', encrypted_content, '\n')

# Specify the decryption key
decryption_key = finding_decryption_key()

# Decrypt the content
decrypted_content = decrypt(encrypted_content, decryption_key)

# Write decrypted content to a Python file
ouotput_file_path = 'decrypted_code.py'
with open(ouotput_file_path, 'w') as file:
    file.write(decrypted_content)
    print('Decrypted_content: \n', decrypted_content)
