import xlrd

data = xlrd.open_workbook(r"E:\pycharm\CRM\data\client.xlsx")
table = data.sheet_by_name("Sheet1")
list = []
for n_row in range(1,table.nrows):
    list.append(table.row_values(n_row))
print(list)