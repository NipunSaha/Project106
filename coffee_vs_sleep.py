import numpy as np
import plotly.express as px
import csv

def plot_fig(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()

def get_data_source(data_path):
    coffee = []
    sleep = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return {
        "x": coffee,
        "y": sleep
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Coffee and Sleep is ",correlation)

def main():
    file_name = "coffeeVsSleep.csv"
    plot_fig(file_name)
    data_source = get_data_source(file_name)
    find_correlation(data_source)

main()