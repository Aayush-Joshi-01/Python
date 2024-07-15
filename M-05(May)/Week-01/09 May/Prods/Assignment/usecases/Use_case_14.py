# You're working on a data analysis tool for a research project.
# Write a Python function to compute the correlation coefficient between two lists of numerical data.

import math


def correlation_coefficient(list1, list2):
    n = len(list1)
    sum_x = sum(list1)
    sum_y = sum(list2)
    sum_xy = sum([x * y for x, y in zip(list1, list2)])
    sum_x2 = sum([x ** 2 for x in list1])
    sum_y2 = sum([y ** 2 for y in list2])
    #            n(Σxy)−(Σx)(Σy)
    # r = ----------------------------
    #    (√[nΣx2−(Σx)^2][nΣy2−(Σy)^2])
    numerator = n * sum_xy - sum_x * sum_y
    denominator = math.sqrt((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2))

    if denominator == 0:
        return None
    else:
        return numerator / denominator


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [2, 3, 4, 5, 6]

    corr_coef = correlation_coefficient(list1, list2)

    print("Correlation coefficient: ", corr_coef)
