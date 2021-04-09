#!/usr/bin/python3
import pandas as pd


matrix=pd.read_csv('matrix.csv')
main=pd.read_csv('main.csv')

print(matrix.head())
print(main.head())