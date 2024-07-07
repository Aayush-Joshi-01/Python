import pandas as pd


# dtype = np.dtype([
#     ('pclass', int),
#     ('survived', int),
#     ('name', 'U50'),
#     ('sex', 'U10'),
#     ('age', float),
#     ('sibsp', int),
#     ('parch', int),
#     ('ticket', 'U20'),
#     ('fare', float),
#     ('cabin', 'U20'),
#     ('embarked', 'U1'),
#     ('boat', 'U10'),
#     ('body', float),
#     ('home_dest', 'U50')
# ])

def data_structuring():
    df = pd.read_csv('Week-9/05 July/Prods/Assignment/Project_Titanic_Analysis/Titanic_CSV/titanic3.csv')
    # data = []
    # with open('titanic3.csv', 'r') as file:
    #     read = csv.reader(file)
    #     next(read)
    #     for row in read:
    #         try:
    #             cleaned_row = [col if col else '0' for col in row]
    #             data.append(tuple(cleaned_row))
    #         except ValueError as e:
    #             print(f"Error processing row: {row}, Error: {e}")
    # structured_data = np.array(data, dtype=dtype)
    # return structured_data
    print(df)
    return df


if __name__ == '__main__':
    data_structuring()