# Write a Python class to reverse a string word by word.
#
# str1 = "geeks quiz practice code" #"code practice quiz geeks"

class ReverseWords:
    def __init__(self, string):
        self.string = string

    def reverse_words(self):
        words = self.string.split()
        reversed_words = ' '.join(reversed(words))
        return reversed_words


str1 = "geeks quiz practice code"
reverse_words = ReverseWords(str1)
print(reverse_words.reverse_words())  # prints: code practice quiz geeks
