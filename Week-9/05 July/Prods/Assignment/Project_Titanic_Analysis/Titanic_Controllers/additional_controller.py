class Additonal_Controller:
    def __init__(self):
        pass

    def family_relationships_and_survival(self, df):
        df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
        family_survival = df.groupby('FamilySize')['Survived'].mean() * 100
        return family_survival

    def survival_rate_by_category(self, data, category_col):
        categories = data[category_col].unique()
        survival_rates = []
        for category in categories:
            total_passengers = len(data[data[category_col] == category])
            if total_passengers == 0:
                continue
            survived_passengers = len(data[(data[category_col] == category) & (data['survived'] == 1)])
            survival_rate = survived_passengers / total_passengers
            survival_rates.append((category, survival_rate))
        return survival_rates
