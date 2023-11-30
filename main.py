# Student Name: Richard Galvez
# Student ID: 010611634

import Truck
import Package
import datetime
import csv
from HashMap import HashMap

# Reference/Source citation: https://docs.python.org/3/library/csv.html
with open("csv/WGUPS-Address-Table.csv") as csvfile1:
    address_reader = csv.reader(csvfile1)
    # TEST READING OF CSV FILE
    for row in address_reader:
        print(', '.join(row))

with open("csv/WGUPS-Distance-Table.csv") as csvfile2:
    distance_reader = csv.reader(csvfile2)
    # TEST READING OF CSV FILE
    # for row in distance_reader:
    #    print(', '.join(row))

with open("csv/WGUPS-Package-File.csv") as csvfile3:
    package_reader = csv.reader(csvfile3)
    # TEST READING OF CSV FILE
    for row in package_reader:
        print(', '.join(row))
