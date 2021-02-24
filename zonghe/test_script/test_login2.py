import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


@pytest.fixture(params=DataRead.read_yaml(r"test_data\login.yaml"))
def login_data(request):
    return request.param


#  第二种办法：注册直接放在登录代码里
def test_login(login_data,baserequest,url,db_info):
    # 注册用户
    MySqlOp.delete_user(db_info,login_data['regdata']['mobilephone'])
    Member.register(baserequest,url,login_data['regdata'])

    # 登录
    r = Member.login(baserequest,url,login_data['logindata'])

    # 检查结果
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['msg'] == login_data['expect']['msg']
    Check.equal(r.json(),login_data['expect'],'code,status,msg')

    # 删除注册用户
    MySqlOp.delete_user(db_info,login_data['regdata']['mobilephone'])

