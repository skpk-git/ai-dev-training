# subhashkumar_module1_5.py

# make python function given a string of words and price for a letter. 
# It will shift only letters by one (E.g. a -> b) and 
# return (shifted string, word count, price of string) in dictionary format. 

def shift_string(text, price_per_letter):
    """Shift each letter by one and return string, word count, and price."""

    # Store the shifted characters.
    shifted_characters = []

    # Go through each character in the input string.
    for character in text:

        # Check whether the character is a letter.
        if character.isalpha():

            # Shift lowercase letters by one position.
            if character.islower():
                if character == "z":
                    shifted_character = "a"
                else:
                    shifted_character = chr(ord(character) + 1)

            # Shift uppercase letters by one position.
            else:
                if character == "Z":
                    shifted_character = "A"
                else:
                    shifted_character = chr(ord(character) + 1)

            # Add the shifted letter to the result.
            shifted_characters.append(shifted_character)

        else:
            # Keep spaces, numbers, and punctuation unchanged.
            shifted_characters.append(character)

    # Combine all characters into the shifted string.
    shifted_string = "".join(shifted_characters)

    # Count the number of words in the original string.
    word_count = len(text.split('-'))

    # Calculate the price based on the number of letters.
    letter_count = sum(character.isalpha() for character in text)
    total_price = letter_count * price_per_letter

    # Return the results in dictionary format.
    result = {
        "shifted_string": shifted_string,
        "word_count": word_count,
        "price": total_price
    }
    return result


# Test the function.
result = shift_string("Hello World v", 2)

# Display the result.
print(result)