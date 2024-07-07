class Class_Controller:

    @staticmethod
    def passenger_demographics_by_class(df):
        class_demographics = df.groupby('pclass').agg({'age': 'mean', 'sex': 'value_counts'})
        return class_demographics
    
    @staticmethod
    def survival_rates_by_class_and_gender(df):
        survival_rates = df.groupby(['pclass', 'sex'])['survived'].mean() * 100
        return survival_rates
    
    @staticmethod
    def fare_analysis_by_class(df):
        fare_analysis = sns.boxplot(x='pclass', y='fare', data=df)
        plt.title('Fare Analysis by Class')
        plt.show()
