from t1 import Log

def lgi():
    data = {'username': '唐马儒', 'password': '123456'}
    aser = ['登录成功', '密码错误']
    Log('http://localhost:8080/jwshoplogin/user/login.do', data, aser).post()  # 登录

    data = {'username': '唐马儒', 'password': '123456', 'email': '610@qq.com', 'phone': '13230000000',
            'question': '哈', 'answer': '哈'}
    aser = ['注册成功', '用户名已经存在']
    Log('http://localhost:8080/jwshoplogin//user/register.do', data, aser).post()  # 注册


if __name__ == '__main__':
    lgi()