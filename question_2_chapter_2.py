def separate_and_convert(input_string):
    """
    Separates an input string into number and letter components.
    Converts even numbers to ASCII code decimal values and upper-case letters to ASCII code decimal values.

    Parameters:
    - input_string (str): The input string containing alphanumeric characters.

    Returns:
    - number_string (str): String containing only the numeric characters from the input.
    - letter_string (str): String containing only the alphabetic characters from the input.
    - even_numbers (list): List of even numeric characters extracted from the number string.
    - ascii_values_numbers (list): List of ASCII code decimal values corresponding to even_numbers.
    - upper_case_letters (list): List of upper-case alphabetic characters extracted from the letter string.
    - ascii_values_letters (list): List of ASCII code decimal values corresponding to upper_case_letters.
    """
    # Separate numbers and letters
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    # Extract even numbers from the number string
    even_numbers = [int(char) for char in number_string if int(char) % 2 == 0]

    # Convert even numbers to ASCII Code Decimal Values
    ascii_even_numbers = [ord(str(number)) for number in even_numbers]

    # Extract upper-case letters from the letter string
    upper_case_letters = [char for char in letter_string if char.isupper()]

    # Convert upper-case letters to ASCII Code Decimal Values
    ascii_upper_case_letters = [ord(char) for char in upper_case_letters]

    return number_string, letter_string, even_numbers, ascii_even_numbers, upper_case_letters, ascii_upper_case_letters

# Input string
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
result = separate_and_convert(input_string)

# Print the results
print("Number String:", result[0])
print("Letter String:", result[1])
print("Even Numbers:", result[2])
print("ASCII Values of Even Numbers:", result[3])
print("Upper-case Letters:", result[4])
print("ASCII Values of Upper-case Letters:", result[5])


def decrypt_cryptogram(cryptogram, shift):
    """
    Decrypts a given cryptogram using a Caesar cipher with the specified shift.

    Parameters:
    - cryptogram (str): The input encrypted text.
    - shift (int): The Caesar cipher shift value.

    Returns:
    - decrypted_text (str): The decrypted text.
    """
    decrypted_text = ''  # Initialize an empty string to store the decrypted result
    for char in cryptogram:
        if char.isalpha():  # Check if the character is alphabetic
            if char.islower():
                # Decrypt lowercase characters using Caesar cipher formula
                decrypted_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            else:
                # Decrypt uppercase characters using Caesar cipher formula
                decrypted_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        else:
            # Non-alphabetic characters are appended unchanged
            decrypted_text += char
    return decrypted_text


def find_shift_key(cryptogram):
    """
    Tries all possible shift values to find the original quote.

    Parameters:
    - cryptogram (str): The input encrypted text.

    Prints:
    - Decrypted text for each shift value.
    """
    for shift in range(1, 26):  # Iterate through shift values from 1 to 25
        decrypted_text = decrypt_cryptogram(cryptogram, shift)
        print(f"Shift {shift}: {decrypted_text}")


# Provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAONG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"

# Find the shift key that gives the original quote
find_shift_key(cryptogram)

