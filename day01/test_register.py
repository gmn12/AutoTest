'''
pytest命名约束：
1.文件用test_开头
2.类用Test开头
3.函数或方法用test_开头
'''


import requests
import pytest

cs = [
    # 注册成功
    {"data": {"mobilephone": "18678564398", "pwd": "123456"},
     "expect": {"status": 1, "code": "10001", "data": None, "msg": "注册成功"}},

    # 密码长度小于6位
    {"data":{"mobilephone":"18678564398","pwd":"12345"},
    "expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},

    # 密码长度大于18位
    {"data": {"mobilephone": "18678564398", "pwd": "1234567890123456789"},
    "expect": {"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}},

    # 密码为空
    {"data": {"mobilephone": "18678564398", "pwd": ""},
     "expect": {"status": 0, "code": "20103", "data": None, "msg": "密码不能为空"}},

    # 手机号码格式不正确
    {"data": {"mobilephone": "1867856439", "pwd": "123456"},
     "expect": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}

]

@pytest.fixture(params=cs)
def register_data(request):
    return request.param

def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.get(url,data)
    return r


# 数据驱动的测试模型
# test_register测试脚本/测试逻辑，测试数据与测试逻辑分离，相同逻辑的数据库放到一起，实现一个脚本即可
# 数据可以放到csv、xml、yaml...去维护
# 注册测试用例
def test_register(register_data):
    print(f"测试数据:{register_data['data']}")
    print(f"预期结果:{register_data['expect']}")
    r = register(register_data['data'])
    assert r.json()['status'] == register_data['expect']['status']
    assert r.json()['code'] == register_data['expect']['code']
    assert r.json()['msg'] == register_data['expect']['msg']


