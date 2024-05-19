# You're developing a program to process student exam scores.
# Write a Python function to determine the median score from a list of scores?

def median(scores):
    scores.sort()
    n = len(scores)
    if n % 2 == 0:
        median = (scores[n // 2 - 1] + scores[n // 2]) / 2
    else:
        median = scores[n // 2]
    return median

if __name__ == '__main__':
    scores = [85, 90, 78, 92, 88, 76, 95, 89]
    median_score = median(scores)
    print(f"The median score is {median_score}.")
