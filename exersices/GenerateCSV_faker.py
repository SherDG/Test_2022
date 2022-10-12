#!/usr/bin/python
import csv
import random
from faker import Faker
fake = Faker()

fieldnames = ['id', 'name', 'age', 'city']
csvfile = open("people_csv.csv", "w")

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

records = 10
for i in range(0, records):
    writer.writerow(
        {'id': str(i), 'name': fake.name(), 'age': str(random.randint(18, 99)), 'city': fake.city()})

csvfile.close()
