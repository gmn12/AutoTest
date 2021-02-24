'''
更灵活的一种测试前置和后置
    可以不用setup、teardown的方式命名
    使用起来灵活
    @pytest.fixture()  yield
'''
import pytest

# 测试前置:测试之前的环境准备、环境初始化、测试数据准备等
# 测试后置:测试结束后环境恢复等
# fixture(scope='function')默认function级别（每个用例都会执行）
@pytest.fixture()
def login():
    print("登录系统")
    yield       # yield之前是前置，之后是后置
    print("退出登录")
    print("退出系统")

def test_query():
    print("查询功能，不需要登录")

def test_add(login):
    print("添加功能，需要登录")

@pytest.mark.usefixtures('login')
def test_delete():
    print("删除功能，需要登录")
# 和上边功能一样
# def test_delete(login):
#     print("删除功能，需要登录")


def test_register():
    print("注册功能，不需要登录")