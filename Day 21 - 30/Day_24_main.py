import csv
import pandas


data = pandas.read_csv("test.txt")
# data_dict = data.to_dict()

print(data[data.dagim == "Monday"])
