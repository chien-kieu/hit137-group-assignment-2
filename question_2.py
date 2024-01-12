# import time
# from PIL import Image

# # Load the original image
# original_image_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/chapter1.jpg'
# original_image = Image.open(original_image_path)

# # Get the size of the image
# width, height = original_image.size

# # Generate a number (n)
# current_time = int(time.time())
# generated_number = (current_time % 100) + 50

# # If the generated number is even, add 10 to it
# if generated_number % 2 == 0:
#     generated_number += 10

# # Create a new image with the modified pixel values
# new_image = Image.new('RGB', (width, height))

# for y in range(height):
#     for x in range(width):
#         # Get the original pixel values (r, g, b)
#         original_pixel = original_image.getpixel((x, y))

#         # Modify the pixel values by adding the generated number
#         modified_pixel = (
#             original_pixel[0] + generated_number,
#             original_pixel[1] + generated_number,
#             original_pixel[2] + generated_number
#         )

#         # Set the modified pixel values in the new image
#         new_image.putpixel((x, y), modified_pixel)

# # Save the new image
# new_image_path = '/Users/chienkieu/Desktop/CDU/SS23/HIT137/Assignment_2/chapter1out.png'
# new_image.save(new_image_path)

# # Calculate the sum of red (r) pixel values in the new image
# red_pixel_sum = sum([pixel[0] for pixel in new_image.getdata()])

# # Print the sum of red pixel values
# print("Sum of Red (r) Pixel Values in the New Image:", red_pixel_sum)

'''
Chapter 2
'''
# def separate_and_convert(input_string):
#     # Separate numbers and letters
#     number_string = ''.join([char for char in input_string if char.isdigit()])
#     letter_string = ''.join([char for char in input_string if char.isalpha()])

#     # Convert even numbers in the number string to ASCII Code Decimal Values
#     even_numbers = [int(char) for char in number_string if int(char) % 2 == 0]
#     ascii_values_numbers = [ord(str(number)) for number in even_numbers]

#     # Convert upper-case letters in the letter string to ASCII Code Decimal Values
#     upper_case_letters = [char for char in letter_string if char.isupper()]
#     ascii_values_letters = [ord(char) for char in upper_case_letters]

#     return number_string, letter_string, ascii_values_numbers, ascii_values_letters

# # Example usage
# input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
# result = separate_and_convert(input_string)

# # Print the results
# print("Number String:", result[0])
# print("Letter String:", result[1])
# print("ASCII Values of Even Numbers:", result[2])
# print("ASCII Values of Upper-case Letters:", result[3])

def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def find_shift_key(cryptogram):
    for shift in range(1, 26):
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted_text}")

# Provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the shift key that gives the original quote
find_shift_key(cryptogram)

