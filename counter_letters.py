# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/18/2024
# Define a function named count_letters that takes as a parameter a string and returns
# A dictionary that tabulates how many of each letter is in that string.

def count_letters(input_string):
    """
    Parameters:
    input_string (str): The string to process, which may contain letters and other characters.

    Returns:
    dict: Dictionary that tabulates the uppercase letters and the values are the counts of each letter.
    """
    # Convert the string to uppercase for the case-insensitivity
    normalized_string = input_string.upper()

    #Initialize an empty dictionary for letter counts
    letter_counts = {}

    # Create the for loop to check if the character is a letter
    # If yes, update the dictionary
    for char in normalized_string:
        if 'A' <= char <= 'Z':
            if char in letter_counts:
                letter_counts[char] +=1 # Increment the count
            else:
                letter_counts[char] = 1 # Add each letter with a count of 1

    # Return the final dictionary
    return count_letters
