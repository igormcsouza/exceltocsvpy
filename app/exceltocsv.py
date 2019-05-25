import os, sys

import openpyxl
import csv

def convert(file='test.xlsx', csv_name="csvfile.csv"):
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))

    wb = openpyxl.load_workbook(os.path.join(dirname, file))
    sh = wb.get_active_sheet()
    with open(os.path.join(dirname, csv_name), 'w', newline="") as f:  # open(csv_name, 'wb') for python 2
        c = csv.writer(f)
        for r in sh.rows:
            c.writerow([cell.value for cell in r])