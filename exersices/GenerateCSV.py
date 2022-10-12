#!/usr/bin/python
import csv
import random

fieldnames = ['id', 'name', 'age', 'city']
csvfile = open("people_csv.csv", "w")

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

names = ['Yulia', 'Stas', 'Max', 'Olga', 'Serg', 'Kate']
cities = ['Dnipro', 'Odesa', 'Kyiv', 'Kharkiv']

records = 100
for i in range(0, records):
    writer.writerow(
        {'id': str(i), 'name': random.choice(names), 'age': str(random.randint(24, 26)), 'city': random.choice(cities)})

csvfile.close()
