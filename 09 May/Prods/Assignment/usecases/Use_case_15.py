# You're developing a data processing tool for a genetics research project.
# Write a Python function to filter out DNA sequences from a list of sequences based on their length.)
def filter_sequences_by_length(sequences, min_length):
    filtered_sequences = []
    for sequence in sequences:
        if len(sequence) >= min_length:
            filtered_sequences.append(sequence)
    return filtered_sequences

if __name__ == '__main__':
    sequences = [
        'ATGCGATCGATCGATCGATCGATCG',
        'ATG',
        'ATGCGATCGATCGATCGATCGATCGATCGATCG',
        'ATGTCGATCG',
        'ATG',
    ]

    min_length = 10

    filtered_sequences = filter_sequences_by_length(sequences, min_length)
    print(filtered_sequences)
