POSITIVE_WORDS = {'good', 'nice', 'great', 'amazing'}


def segregate_positive_words(reviews: list) -> list:
    review_words = set()
    for review in reviews:
        extracted_words = extract_words(review)
        for words in extracted_words:
            review_words.add(words.lower())
    result = list(review_words.intersection(POSITIVE_WORDS))
    return result


def extract_words(review):
    return review.split()


if __name__ == '__main__':
    reviews = ["It's a great product", "Amazing to use", "Nice feel to it", "Good Quality stuff", "Quality is amazing",
               "Feels Great to Use"]
    print(segregate_positive_words(reviews))
