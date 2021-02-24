'''
day02->新建文件夹->新建conftest.py
fixture: session级别的后置和前置，(所有测试文件只执行一次)放到conftest.py文件中
不需要import .pytest 根据文件名字找对应的方法
脚本层的一些公共方法，可以放到这里
conftest.py作用域：对当前所在的文件的目录下的测试文件生效
一个工程可包含多个conftest.py
'''
import pytest

@pytest.fixture(scope='session')
def db():
    print("前置：连接数据库")
    yield
    print("后置:断开数据库连接")

@pytest.fixture(scope='session')
def login():
    print("前置，在首次使用login的地方执行前置")
    yield
    print("后置，模块所有用例执行完之后执行后置")