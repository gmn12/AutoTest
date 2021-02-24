# 金融：注册用户 ->登录->充值1000->取现100(服务器异常)
from unittest import mock

import pytest
import requests

cs = [
    {"data":{"mobilephone": "15634983215",
    "pwd": "123456"},"expect":{"status":1,"code":'10001',"msg":"注册成功"}}
]

@pytest.fixture(params=cs)
def datas(request):  # 固定写法
    return request.param  # 固定写法


def test_register(datas):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url,data=datas['data'])
    print(r.text)
    assert r.json()['status'] == datas['expect']['status']
    assert r.json()['code'] == datas['expect']['code']
    assert r.json()['msg'] == datas['expect']['msg']
def test_login(datas):
    url = "http://jy001:8081/futureloan/mvc/api/member/login"
    r = requests.post(url,data=datas['data'])
    assert r.json()['msg'] == "登录成功"
def test_recharge(datas):
    data = {"mobilephone":datas['data']['mobilephone'],"amount":1000}
    url = "http://jy001:8081/futureloan/mvc/api/member/recharge"
    r = requests.post(url, data=data)
    assert r.json()['status']==1
def test_withdraw(datas):
    data = {"mobilephone":datas['data']['mobilephone'],"amount":100}
    url = "http://jy001:8081/futureloan/mvc/api/member/withdraw"
    r1 = mock.Mock(return_value={"status":1,"code":'20102'})
    r = r1(data)
    print(r)



