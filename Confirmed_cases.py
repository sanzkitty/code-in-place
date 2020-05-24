import pandas as pd
from matplotlib import pyplot as plt

def main():
    data = pd.read_csv("daily confirmed cases.csv")
    data.head()
    data['date'] = pd.to_datetime(data['date'])
    data['week'] = data['date'].dt.week
    data.groupby('week').count()['new_cases']
    usa = data[data.location == "United States"]
    china = data[data.location == "China"]
    japan = data[data.location == "Japan"]
    nepal = data[data.location == "Nepal"]
    uk = data[data.location == "United Kingdom"]
    plt.plot(usa.date, usa.new_cases)
    plt.plot(china.date, china.new_cases)
    plt.plot(japan.date, japan.new_cases)
    plt.plot(nepal.date, nepal.new_cases)
    plt.plot(uk.date, uk.new_cases)
    plt.title("Daily new cases of COVID-19")
    plt.xlabel("Dates")
    plt.ylabel("Number of new cases")
    plt.legend(["U.S.A", "China", "Japan", "Nepal", "United Kingdom"])
    plt.show()


if __name__ == '__main__':
    main()