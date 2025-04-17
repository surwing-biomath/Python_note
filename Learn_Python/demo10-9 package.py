import openpyxl

workbook = openpyxl.load_workbook('weather.xlsx')
sheet = workbook['天气预报']
lst = []
for row in sheet.rows:
    sublst = []
    for cell in row:
        sublst.append(cell.value)
    lst.append(sublst)

for item in lst:
    print(item)