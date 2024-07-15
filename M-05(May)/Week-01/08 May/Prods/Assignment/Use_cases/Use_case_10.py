# You are developing a text processing tool that requires identifying
# the most common word in a given text. Implement a Python function to
# find the most frequent word in a text string, excluding common stop
# words such as "the", "is", "and", etc.
import re
from collections import Counter


def find_most_frequent_word(text: str, stopwords: set = None) -> str:
    if stopwords is None:
        stopwords = {"the", "is", "and", "are", "am", "a", "an", "in", "it", "you", "i", "to", "of", "for", "on",
                     "that", "with", "was", "he", "she", "as", "his", "her", "its", "had", "have", "has", "but", "not",
                     "be", "were", "by", "at", "so", "we", "they", "my", "your", "from", "who", "which", "there", "or",
                     "us", "this", "him", "me", "what", "why", "how", "when", "where", "up", "down", "out", "off",
                     "over", "under", "again", "then", "once", "here", "there", "all", "any", "both", "each", "few",
                     "more", "most", "other", "some", "such", "no", "nor", "only", "own", "same", "so", "than", "too",
                     "very", "can", "will", "just", "don", "should", "now"}
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = [word for word in text.split() if word not in stopwords]
    word_counts = Counter(words)
    print(word_counts.most_common(1))
    most_frequent_word = word_counts.most_common(1)[0][0]
    return most_frequent_word


text = "The quick brown fox jumps over the lazy dog. The dog is not lazy, it's just tired."
most_frequent_word = find_most_frequent_word(text)
print("The most frequent word is:", most_frequent_word)
