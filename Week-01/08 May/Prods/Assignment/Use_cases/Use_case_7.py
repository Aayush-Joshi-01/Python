#  You are developing a program to process user input. Implement a
# Python function to find the most frequent word in a given text string.
import string


def extract_words(text):
    # Replace punctuation characters with a space and convert to lowercase
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    # Split the text into words using space as a separator
    words = text.split()

    return words


def most_frequent_word(text):
    # Extract words from the text string
    words = extract_words(text)
    # Count the occurrences of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # Find the most frequent word
    max_count = max(word_counts.values())
    most_frequent = [word for word, count in word_counts.items() if count == max_count]
    return most_frequent[0] if most_frequent else None


# Example usage:
text = "Hello, World! This is a test string. We're processing user input for a search feature. Hello, again!"
print(most_frequent_word(text))
