"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os

import pytest
import yaml


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
from pythoncode.calculator import Calculator


@pytest.fixture(autouse=True)
# @pytest.fixture(autouse=True)
def  function_fixture():
    print("开始计算")
    yield '123'
    print("结束计算")

@pytest.fixture(scope='module')
# @pytest.fixture(autouse=True)
def  module_fixture():
    # calc = Calculator()
    yield
    print("测试结束")

@pytest.fixture()
def get_datas():
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'datas/datas_ymm.yml'),encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        out_of_index_datas =datas['add']['out_of_index']
        boundary_effective_value_datas =datas['add']['boundary_effective_value']
        all_positive_integer_datas = datas['add']['all_positive_integer']
        return out_of_index_datas,boundary_effective_value_datas,all_positive_integer_datas



