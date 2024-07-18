import csv
import pandas as pd

with open ('files/sample.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

df = pd.read_csv('files/sample.csv')
print(df)

with open ('files/sample.csv', 'a') as csv_file:
    writer_var = csv.writer(csv_file)
    writer_var.writerow(['7', 'Jubayer', 'Engineering', 'Web Developer', '73000'])

df = pd.read_csv('files/sample.csv')
print(df)