'''

'''

import requests

# 表单格式的数据：content-type:www-x-form-urlencoded,使用data传参
# 登录接口
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {
    "mobilephone":"15908761908",
    "pwd":"123456"
}
# 发送请求
r = requests.post(url,data=cs)
print(r.text)
rjson = r.json()
assert rjson["status"] == 1
assert rjson["code"] == '10001'
assert rjson["msg"] == '登录成功'

# json格式的数据，content-type:applicatioon/json,使用json传参
# 具体使用data还是json传参，要看接口怎么定义
# httpbin.org 是一个测试网站，封装成json格式的返回

url = "http://www.httpbin.org/post"
cs ={
    "mobilephone":"15908761908",
    "pwd":"123456"
}
r = requests.post(url,data=cs)
# print("data传参==",r.text)
r = requests.post(url,json=cs)
# print("json传参==",r.text)
# carnumber=12&cartype=12&color=12&carimg=images%2Fdefaultcarimage.jpg&description=12&price=12&rentprice=12&deposit=12&isrenting=0


# ---------------租车系统 ，添加车辆 ------------------
url = "http://127.0.0.1:8080/carRental/car/addCar.action"
# 接口文档中对接口描述不清晰
# 通过界面操作借口对应的功能，抓包（Fiddler、浏览器F12）看
cs = {
      "carnumber":"mn987608",
    "cartype":"12345"  ,
    "color":"123435"    ,
    "carimg" :"images%2Fdefaultcarimage.jpg"  ,
    "description"  :"12345"   ,
    "price" :"12345"  ,
     "rentprice":"12345",
    "deposit":"12345" ,
    "isrenting":"0"
}

# 使用接口添加的车辆，中文字符乱码，但是用界面添加的车辆，不会有乱码
# 分别抓接口的包，与界面的包，对比差异，界面设置了charset=UTF-8，但是脚本未设置导致
# 设置字符集为charset=UTF-8
# 请求头格式是key-value格式的
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"  ,
    "User-Agent" :"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
# Fiddler抓脚本的包，设置代理
proxy = {
    "http":"http://127.0.0.1:8888",   #http协议，使用这个代理
    "https":"http://127.0.0.1:8888"   #https协议，使用这个代理
}
r = requests.post(url,data=cs,headers = head,proxies=proxy)

print(r.text)
rjson = r.json()
assert  rjson["code"] == -1
assert  rjson["msg"] =="添加失败"