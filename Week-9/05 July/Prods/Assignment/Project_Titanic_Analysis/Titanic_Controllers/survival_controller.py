class Survival_Controller:
    def overall_survival_rate(arr):
        survived_count = arr['survived'].sum()
        total_passengers = arr['survived'].shape
        survival_rate = (survived_count / total_passengers) * 100
        return survival_rate

    def survival_by_class(df):
        survival_by_class = df.groupby('pclass')['survived'].mean() * 100
        return survival_by_class

    def survival_by_gender(df):
        survival_by_gender = df.groupby('sex')['survived'].mean() * 100
        return survival_by_gender

    def survival_by_age_group(df, bins=[0, 18, 30, 50, 100]):
        df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=['0-18', '19-30', '31-50', '51+'])
        survival_by_age_group = df.groupby('aAgeGroup')['survived'].mean() * 100
        return survival_by_age_group

    def survival_by_family_size(df):
        df['FamilySize'] = df['sibsp'] + df['parch'] + 1
        survival_by_family_size = df.groupby('FamilySize')['survived'].mean() * 100
        return survival_by_family_size