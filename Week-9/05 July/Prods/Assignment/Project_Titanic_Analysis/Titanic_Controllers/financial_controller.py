class Financial_Controller:
    def ticket_fare_distribution(df):
        fare_distribution = df['fare'].plot(kind='hist', bins=20, edgecolor='black')
        plt.xlabel('fare')
        plt.title('Ticket Fare Distribution')
        plt.show()

    def average_fare_by_class(df):
        average_fare_by_class = df.groupby('pclass')['fare'].mean()
        return average_fare_by_class

    def fare_vs_survival(df):
        fare_vs_survival = sns.boxplot(x='survived', y='fare', data=df)
        plt.title('Fare vs. Survival')
        plt.show()