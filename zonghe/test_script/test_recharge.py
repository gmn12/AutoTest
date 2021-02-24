'''
测试充值的脚本
'''
import pytest
#
from zonghe.baw import Member
from zonghe.caw import DataRead, MySqlOp, Check

@pytest.fixture(params=DataRead.read_yaml(r"test_data\recharge_data.yaml"))
def recharge_data(request):
    return request.param

def test_recharge(recharge_data,baserequest,url,db_info):
    # 注册用户
    MySqlOp.delete_user(db_info,recharge_data['regdata']['mobilephone'])
    Member.register(baserequest,url,recharge_data['regdata'])
    # 登录用户
    Member.login(baserequest,url,recharge_data['logindata'])
    # 充值
    r = Member.recharge(baserequest,url,recharge_data['rechdata'])
    # 校验结果
    Check.equal(r.json(),recharge_data['expect'],'code,status,msg')
