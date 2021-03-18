import pandas as pd
import numpy as np

p = "abacate"
for test in p:
  print(test)
  print('***')
print('fim')
import csv

with open('.csv') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_reader.__next__()

    for row in csv_reader:
        print( row[0] + ', ' + row[1] + ', ' + row[2] )