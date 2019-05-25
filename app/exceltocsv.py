import os, sys

import openpyxl
import csv

def convert(file='test.xlsx', csv_name="csvfile.csv"):
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))

    wb = openpyxl.load_workbook(os.path.join(dirname, file))
    sh = wb.get_active_sheet()

    if sys.version_info[0] == 2:
        with open(csv_name, 'wb') as f:  
            c = csv.writer(f)
            for r in sh.rows:
                c.writerow([cell.value for cell in r])

    if sys.version_info[0] == 3:
        with open(os.path.join(dirname, csv_name), 'w', newline="") as f:
            c = csv.writer(f)
            for r in sh.rows:
                c.writerow([cell.value for cell in r])