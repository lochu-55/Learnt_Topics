import csv
from pathlib import Path

basedir = Path(__file__).resolve().parent.parent
datafile = basedir.joinpath('config').joinpath('data.csv')

def get_data():
    with open(datafile,'r') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]

    return data