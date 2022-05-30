import time
import  os

import pytest
import yaml
from selenium import  webdriver


ph = os.path.dirname(os.path.abspath(__file__))
@pytest.fixture()
def get_yml_datas():
    with open(ph+'\datas\data.yml',encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        return datas
# print(get_yml_datas())

def pytest_addoption(parser):
    mygroup = parser.getgroup('BrowserType')
    mygroup.addoption('--browser-type',
                      default='google',
                      dest='google',
                      help="指定脚本运行浏览器")
@pytest.fixture()
def get_command_line_browser_type(request):
    return request.config.getoption("--browser-type")
