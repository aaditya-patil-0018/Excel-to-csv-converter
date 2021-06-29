import pandas as pd
import csv

xlFileName = str(input('Enter name for Excel file : '))

try:
    xlFile = pd.read_excel(f"{xlFileName}.xls")
except FileNotFoundError:
    print('Excel file not found!')
    quit()

for i in xlFile:
    if 'Unnamed' in i:
        xlFile.drop(i, axis=True, inplace=True)

rows = xlFile.shape[0]
columns = xlFile.shape[1]

csvFileName = str(input('Enter name for csv file : '))

csvFile = f"{csvFileName}.csv"

for i in range(int(rows)):
    r = xlFile.iloc[i]
    with open(csvFile, 'a') as cf:
        c_writer = csv.writer(cf)
        if i == 0:
            c_writer.writerow(xlFile.columns)
        c_writer.writerow(r)

#print('Script ran Successfully')
