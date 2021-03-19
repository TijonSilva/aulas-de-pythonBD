import pandas as pd
import numpy as np

p = "abacate"
for test in p:
  print(test)
  print('***')
print('fim')
import csv
teste = pd.read_csv('plandados.csv', delimiter= ';', decimal= ',')
print (teste)