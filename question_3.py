# total = 0

# for i in range(5):
#     for j in range(3):
#         if i + j == 5:
#             total += i + j
#         else:
#             total -= i - j

# counter = 0
# while counter < 5:
#     if total < 13:
#         total += 1
#     elif total > 13:
#         total -= 1
#     else:
#         counter += 2

# print(total)

# def encrypt(text, key):
#     encrypted_text = ""
#     for char in text:
#         if char.isalpha():
#             shifted = ord(char) + key
#             if char.islower():
#                 if shifted > ord('z'):
#                     shifted -= 26
#                 elif shifted < ord('a'):
#                     shifted += 26
#             elif char.isupper():
#                 if shifted > ord('Z'):
#                     shifted -= 26
#                 elif shifted < ord('A'):
#                     shifted += 26
#             encrypted_text +=chr(shifted)
#         else:
#             encrypted_text += char
#     return encrypted_text
    
# key = 13


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

key = 13
# original_code = 'def'
# encrypted_code = encrypt(original_code, key)
# print(f'Encrypted code: {encrypted_code}')

# decrypted_code = decrypt(encrypted_code, key)
# print(f'Decrypted code: {decrypted_code}')

# Read encrypted content from a text file
encrypted_file_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/hit137-group-assignment-2/encrypted_code.text'
with open(encrypted_file_path, 'r') as file:
    encrypted_content = file.read()

# Specify the decryption key
decryption_key = 13

# Decrypt the content
decrypted_content = decrypt(encrypted_content, decryption_key)

# Write decrypted content to a Python file
python_file_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/hit137-group-assignment-2/decrypted_code.py'
with open(python_file_path, 'w') as file:
    file.write(decrypted_content)
