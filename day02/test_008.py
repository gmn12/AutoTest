'''
fixture 可以带参数
'''
import pytest

# 5组测试数据，表示不同的用户名
@pytest.fixture(params=["root","admin","administrator","123","Test-123"])
def login_data(request): # 固定写法 request 是pytest中的关键字，将数据取出来传到test_login里
    return request.param # 固定写法


# 使用5组数据分别执行这个用例，共执行5次
def test_login(login_data):
    print(login_data)
    # format,
    print(f"测试登录功能，使用用户名：{login_data}登录")
    # print("测试登录功能，使用用户名：%s登录"%{login_data})  #和上班效果相同

#     用字典来实现
@pytest.fixture(params=[{"username":"root","pwd":"123456"},{"username":"admin","pwd":"123456"}])
def login_data2(request): # 固定写法 request 是pytest中的关键字，将数据取出来传到test_login里
    return request.param # 固定写法

def test_login2(login_data2):
    # print(login_data2)
    print(f"测试登录功能，使用用户名：{login_data2['username']},密码：{login_data2['pwd']}登录")
