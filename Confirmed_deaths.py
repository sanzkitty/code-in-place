import pandas as pd
from matplotlib import pyplot as plt

def main():
    data = pd.read_csv("daily-covid-cases-deaths.csv")
    data.head()
    data['date'] = pd.to_datetime(data['date'])
    data['week'] = data['date'].dt.week
    data.groupby('week').count()['daily_cases']
    usa = data[data.location == "United States"]
    china = data[data.location == "China"]
    japan = data[data.location == "Japan"]
    nepal = data[data.location == "Nepal"]
    uk = data[data.location == "United Kingdom"]
    plt.plot(usa.date, usa.daily_deaths)
    plt.plot(china.date, china.daily_deaths)
    plt.plot(japan.date, japan.daily_deaths)
    plt.plot(nepal.date, nepal.daily_deaths)
    plt.plot(uk.date, uk.daily_deaths)
    plt.title("Daily confirmed death cases of COVID-19")
    plt.xlabel("Dates")
    plt.ylabel("Number of new deaths")
    plt.legend(["U.S.A", "China", "Japan", "Nepal", "United Kingdom"])
    plt.show()


if __name__ == '__main__':
    main()