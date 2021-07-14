import xlwings as xw

'''单个值插入
sht.range('A1').value = '产品名称'
sht.range('B1').value = '编号'
sht.range('C1').value = '价格'

插入一行
sht.range('a1').value = [1,2,3,4]
等同于
sht.range('a1:d4').value = [1,2,3,4]
# 插入一列
# sht.range('a2').options(transpose=True).value = [5,6,7,8]

# 同时插入行列
# sht.range('a6').expand('table').value = [['a','b','c'],['d','e','f'],['g','h','i']]'''

class excl():
    def exlprint(self):
        app=xw.App(visible=False, add_book=False) # add_book也就是是否增加excel 的book ; visible=True 表示操作过程是否可显示
        wo=app.books.open(r'C:\Users\Administrator\Desktop\testdata1.xlsx')
        sht=wo.sheets['Sheet1']
        # 获取用户sheet1中的 sht.used_range.value.last_cell.row 所有行数；.last_cell.colum (列数)
        self.dat = []
        self.dat = sht.range('A2').expand().value  # 跳过第一行表格标题，从A2行开始读取所有已使用单元格 sht.range('A2').expand().value
        '''data = sht.used_range().value # 读取所有已使用的单元格'''
        # print(self.dat)

        app.quit()

if __name__ == '__main__':
    e=excl()
    e.exlprint()
    e.exlx()