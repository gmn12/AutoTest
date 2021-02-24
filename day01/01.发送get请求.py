'''
接口测试：
    使用request中的get、post方法调用接口，检查返回值是否正确
'''

import requests

# ------------------get请求，不带参数的------------------
# 获取用户列表的接口
url = "http://jy001:8081/futureloan/mvc/api/member/list"
# 发送get请求
r = requests.get(url);
# 打印响应，文本格式的
# print(r.text)
# 断言:检查结果是否与预期相同
assert r.status_code == 200
assert r.reason == "OK"
# 转成json格式，打印响应体，当做字典来用
rjson = r.json()
assert rjson["status"] ==1
assert rjson["code"] =='10001'
assert rjson["msg"] == "获取用户列表成功"
# 响应头
print(r.headers)

# ------------------------get请求，带参数的------------------------
# 注册接口，参数拼接在URL后边 ?后边是参数，多个参数用 & 连接
# url ="http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15908761908&pwd=123456"
# # 发送get请求
# r = requests.get(url)
# # 打印响应，文本格式
# print(r.text)
# # 转成json格式
# rjson = r.json()
# assert rjson["status"] == 1
# assert rjson["code"] == '10001'
# assert rjson["msg"] == '注册成功'
#
# # 注册接口，使用param传参
# url = "http://jy001:8081/futureloan/mvc/api/member/register"
# cs = {
#     "mobilephone":"15908761908",
#     "pwd":"123456",
#     "regname":"request_test"
# }
# r = requests.get(url,params=cs)
# print(r.text)
# rjson = r.json()
# assert rjson["status"] == 0
# assert rjson["code"] == '20110'
# assert rjson["msg"] == '手机号码已被注册'

# 查询手机号码归属地的接口，参数：tel
url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm?tel=13279255119"
# 发送get请求
r = requests.get(url)
print(r.text)
# print(r.json()) #报错，因为返回的结果不是json格式的
# 断言
# assert '移动' in r.text