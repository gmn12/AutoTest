import requests

# 租车系统里上传图片
# 接口地址
url = "http://127.0.0.1:8080/carRental/file/uploadFile.action"
# 本地存在的文件
file = "d:/test.png"
# rb二进制只读的方式打开
with open(file,mode='rb') as f:
    # ('name':file-tuple)
    # file-tuple:('filename',fileobj,'content_type')
    cs={"mf":(file,f,"image/png")}
    r = requests.post(url,files=cs)
    print(r.text)
    # {"code":0,"msg":"","count":null,"data":{"src":"2021-01-28/202101281428453619307.png_temp"}}
    # 获取图片的路径
    uploadPath = r.json()['data']['src']


# 添加车，使用刚上传的图片
url = "http://127.0.0.1:8080/carRental/car/addCar.action"

cs = {
      "carnumber":"mn98776",
    "cartype":"12345"  ,
    "color":"123435"    ,
    "carimg" :uploadPath  ,
    "description" :"12345"   ,
    "price" :12345,
     "rentprice":12345,
    "deposit":12345,
    "isrenting":0
}
head = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
r = requests.post(url,data=cs,headers = head)
print(r.text)