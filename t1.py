import requests
import xlwings as xw
import json


class Log():
    def exlprint(self):
        app=xw.App(visible=False, add_book=False) # add_book也就是是否增加excel 的book ; visible=True 表示操作过程是否可显示
        wo=app.books.open(r'C:\Users\Administrator\Desktop\testdata1.xlsx')
        sht=wo.sheets['Sheet1']
        # 获取用户sheet1中的 sht.used_range.value.last_cell.row 所有行数；.last_cell.colum (列数)
        self.dat = []
        self.dat = sht.range('A2').expand().value  # 跳过第一行表格标题，从A2行开始读取所有已使用单元格 sht.range('A2').expand().value
        '''data = sht.used_range().value # 读取所有已使用的单元格'''
        return self.dat

        app.quit()
    def post(self):
        for i in range(0, len(self.dat)):
            self.url = self.dat[i][2]
            self.data = self.dat[i][3]
            self.aser = self.dat[i][4]
            self.num = self.dat[i][0]
            # print(self.aser)
            # print(r.text)
            # print(r.status_code)
            r = requests.post(url=self.url, data=self.data.encode())  # 有中文可加  .encode()
            aser_list = self.aser.split(",")
            # print(aser_list)
            for j in range(len(aser_list)):
                # print(aser_list[j])
                # print(r.text)
                if aser_list[j] in r.text:
                    ar=True
                else:
                    ar=False
            if ar==True:
                print(f'{self.num}通过')
            else:
                print(f'{self.num}不通过')






if __name__ == '__main__':
    l = Log()
    l.exlprint()
    l.post()