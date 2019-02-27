import csv
import socket

with open('data/ml-100k.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(f'\t{row[0]} - {row[1]} - {row[2]}')