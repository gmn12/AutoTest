'''
Cookie  用来识别用户
'''
import requests

# 没有登录时调用,返回跳转到登录页面
url = " https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上Cookie信息
head = {
"Cookie":"_ga=GA1.2.585167780.1611729438; _gid=GA1.2.2043552909.1611729438; __auc=fc5fb9c6177428f96a475246db2; MEIQIA_TRACK_ID=1ndqIh78HuhoMQaZXfXGMCyzHGX; __asc=81e105b517747dc9b5f0b2b91e4; MEIQIA_VISIT_ID=1ngiwfkYKVTwE2aeobYZVvoGtou; _gat=1; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611733509,1611736862,1611818376,1611820260; BAGSESSIONID=83c94601-f305-4bd8-9b99-c94085510d50; JSESSIONID=205D7099C2A82E374F778BE535EE8402; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611820270; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_=2780487875@qq.com; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38"
}
r = requests.get(url,headers = head)
print(r.text)
assert "<title>百格活动 - 账户总览</title>"

'''
缺点：
    1.cookie会失效，失效后需要重新获取
    2.登陆后每一个接口都带有cookie
'''