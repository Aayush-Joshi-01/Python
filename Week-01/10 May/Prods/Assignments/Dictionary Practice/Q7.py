def count_items_in_list(d):
    return sum(len(v) for v in d.values())


if __name__ == '__main__':
    dict = {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    print(count_items_in_list(dict))
