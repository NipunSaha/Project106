import numpy as np
import plotly.express as px
import csv

def plot_fig(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def get_data_source(data_path):
    marks = []
    days = []
    with open(data_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            marks.append(float(row["Coffee in ml"]))
            days.append(float(row["sleep in hours"]))
    return {
        "x": marks,
        "y": days
    }

def find_correlation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Marks and Days Present is ",correlation)

def main():
    file_name = "daysVsMarks.csv"
    plot_fig(file_name)
    data_source = get_data_source(file_name)
    find_correlation(data_source)

main()