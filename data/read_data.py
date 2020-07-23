import csv
import xlrd
# txt读取文件
# class ReadData():
def read_txt(file_name):
    with open(file_name, 'r+', encoding='utf-8') as f:
        line = f.readlines()
    return (line)


# csv读取数据
def read_csv(file_name):
    lt = []  # 定义空列表，用户存储读取出来的数据
    with open(file_name, 'r+', encoding='utf-8') as f:
        data = csv.reader(f)  # 读取数据
        for dt in data:  # 读取的数据不能直接使用需要遍历
            lt.append(dt)  # 将结果存储到列表中
    return (lt)


# excl读取文件
def read_excel(file_name,sheet_name):
    lst = []
    table = xlrd.open_workbook(file_name)  # 获取Excel
    sheet = table.sheet_by_name(sheet_name)  # 获取sheet
    row = sheet.nrows  # 所有行
    # col = sheet.ncols#所有列
    # print(row,col)
    for i in range(1, row):
        row_value = sheet.row_values(i)
        lst.append(row_value)
    return (lst)




# user_pwd = read_excel('user.xlsx', 'user')
# print(user_pwd)
# user = user_pwd[0][0]
# pwd = user_pwd[0][1]
# print(user, pwd)
