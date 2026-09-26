#make python code to read the text file you made with people address (Q.6). Then return word count for each address. Append the word count into the same file. 

def count_address_words():
    """Read address.txt, count words in the address, and append the count."""

    # Open the address file in read mode.
    with open("address.txt", "r") as file:
        lines = file.readlines()

    # Find the line that contains the address.
    for line in lines:
        if line.startswith("Address:"):
            # Remove "Address:" from the beginning of the line.
            address = line.replace("Address:", "").strip()

            # Count the number of words in the address.
            word_count = len(address.split())

            # Append the word count to the same file.
            with open("address.txt", "a") as file:
                file.write(f"Address Word Count: {word_count}\n")

            # Display the word count.
            print("Address:", address)
            print("Word Count:", word_count)


# Call the function.
count_address_words()