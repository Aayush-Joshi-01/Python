class Class_Controller:

    @staticmethod
    def passenger_demographics_by_class(df):
        class_demographics = df.groupby('Pclass').agg({'Age': 'mean', 'Sex': 'value_counts'})
        return class_demographics
    
    @staticmethod
    def survival_rates_by_class_and_gender(df):
        survival_rates = df.groupby(['Pclass', 'Sex'])['Survived'].mean() * 100
        return survival_rates
    
    @staticmethod
    def fare_analysis_by_class(df):
        fare_analysis = sns.boxplot(x='Pclass', y='Fare', data=df)
        plt.title('Fare Analysis by Class')
        plt.show()
