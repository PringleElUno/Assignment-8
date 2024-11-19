# Author: Luis Pringle
# GitHub username: PringleElUno
# Date: 11/18/2024
# Define a function named words_in_both that takes two strings as parameters
# And returns a Python set containing only those words that appear in both of the strings.

def words_in_both(string1, string2):
    """
    Parameters:
    string1 (str): The first string to check.
    string2 (str): The second string to check.

    Returns:
    set: A set that contains the words that appear in both of the strings.
    """

    # Split both strings into lowercase words
    words1 = string1.lower().split()
    words2 = string2.lower().split()

    # Convert the lists to sets and find their intersections
    common_words = set(words1) & set(words2)

    # Return the set of common words
    return common_words
