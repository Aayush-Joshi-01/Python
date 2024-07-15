# take input string
# reverse and print
# vowel and consonant count
# count total digits

def get_input_string():
    return input("Enter the string: ")


def reverse_string(string):  # to reverse the string
    reverse_string = string[::-1]
    return reverse_string


def consonant_vowel_count(string):  # Count the Vowels and Consonants and return both
    consonant_count = 0
    vowel_count = 0
    for char in string:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        else:
            consonant_count += 1
    return consonant_count, vowel_count


def count_total_count(string):  # count the characters in a string
    total_count = 0
    for char in string:
        total_count += 1
    return total_count


if __name__ == '__main__':
    string = get_input_string()
    print(f"The reversed string is: {reverse_string(string)}")
    consonant, vowel = consonant_vowel_count(string)
    print(f"The Count Consonant: {consonant} and Count vowel: {vowel}")
    print(f"The Count total character: {count_total_count(string)}")
