import csv
import pandas


data = pandas.read_csv("wether.csv")
# data_dict = data.to_dict()

print(data[data.day == "Monday"])
