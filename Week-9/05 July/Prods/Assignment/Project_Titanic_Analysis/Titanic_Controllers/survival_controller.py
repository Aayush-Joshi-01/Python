import pandas as pd


class Survival_Controller:

    @staticmethod
    def overall_survival_rate(df):
        survived_count = df['survived'].sum()
        total_passengers = df['survived'].count()
        survival_rate = (survived_count / total_passengers) * 100
        return survival_rate

    @staticmethod
    def survival_by_class(df):
        survival_by_class = df.groupby('pclass')['survived'].mean() * 100
        return survival_by_class

    @staticmethod
    def survival_by_gender(df):
        survival_by_gender = df.groupby('sex')['survived'].mean() * 100
        return survival_by_gender

    @staticmethod
    def survival_by_age_group(df, bins=[0, 18, 30, 50, 100]):
        df['AgeGroup'] = pd.cut(df['age'], bins=bins, labels=['0-18', '19-30', '31-50', '51+'])
        survival_by_age_group = df.groupby('AgeGroup')['survived'].mean() * 100
        return survival_by_age_group

    @staticmethod
    def survival_by_family_size(df):
        df['FamilySize'] = df['sibsp'] + df['parch'] + 1
        survival_by_family_size = df.groupby('FamilySize')['survived'].mean() * 100
        return survival_by_family_size
