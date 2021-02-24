'''
测试登录的脚本
'''

import pytest

from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check


# 前置条件，注册的数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_setup.yaml"))
def setup_data(request):
    return request.param

# 登录的测试数据
@pytest.fixture(params=DataRead.read_yaml(r"test_data\login_data.yaml"))
def login_data(request):
    return request.param

# 测试前置与后置，环境准备与清理
@pytest.fixture()
def register(setup_data,baserequest,url,db_info):
    # 注册用户
    MySqlOp.delete_user(db_info,setup_data['data']['mobilephone'])
    r = Member.register(baserequest,url,setup_data['data'])
    # assert r.json()['code'] == setup_data['expect']['code']
    # assert r.json()['status'] == setup_data['expect']['status']
    # assert r.json()['msg'] == setup_data['expect']['msg']
    Check.equal(r.json(),setup_data['expect'],'code,status,msg')

    yield  # 之前是前置，之后是后置
    # 删除注册用户
    MySqlOp.delete_user(db_info,setup_data['data']['mobilephone'])


# 第一种办法，把注册放在前置和后置
def test_login(register,login_data,baserequest,url):
    # 下发登录的请求
    r = Member.login(baserequest,url,login_data['data'])
    # 检查结果
    # assert r.json()['code'] == login_data['expect']['code']
    # assert r.json()['status'] == login_data['expect']['status']
    # assert r.json()['msg'] == login_data['expect']['msg']
    Check.equal(r.json(),login_data['expect'],'code,status,msg')

