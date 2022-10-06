import csv
from pathlib import Path

dataFile = 'data.csv'
configDirectory = 'config'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(configDirectory).joinpath(dataFile)


# print(DATA_FILE)

def get_data():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip first row
        data = [tuple(row) for row in reader]
    return data


print(get_data())
