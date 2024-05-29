def count_vowels(sentence: str) -> dict:
    sentence = sentence.lower()
    vowel = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for word in sentence:
        if word in vowel.keys():
            vowel[word] += 1
    return vowel


if __name__ == '__main__':
    sentence = "Hello Worlds I am here"
    print(count_vowels(sentence))
