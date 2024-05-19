# You're working on a program to analyze survey responses.
# Write a Python function to calculate the mode of a list of responses.

def mode(responses):
    from collections import Counter

    counter = Counter(responses)
    mode = counter.most_common(1)
    if mode:
        return mode[0][0]
    else:
        return None

if __name__ == '__main__':
    responses = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    mode_value = mode(responses)
    print(mode_value)
