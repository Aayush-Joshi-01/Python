class Demographic_Controller:
    def __init__(self):
        pass

    def passenger_count_by_class(self, df):
        passenger_count_by_class = df['pclass'].value_counts().sort_index()
        return passenger_count_by_class

    def gender_distribution(self, df):
        gender_distribution = df['sex'].value_counts()
        return gender_distribution

    def age_distribution(self, df):
        age_distribution = df['age'].plot(kind='hist', bins=20, edgecolor='black')
        plt.xlabel('age')
        plt.title('Age Distribution of Passengers')
        plt.show()

    def embarkation_port_analysis(self, df):
        embarkation_port_counts = df['embarked'].value_counts()
        return embarkation_port_counts