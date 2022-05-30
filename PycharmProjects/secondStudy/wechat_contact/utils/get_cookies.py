import os
import time

import yaml
from selenium import webdriver


def get_cookies(get_datas):
    save_dir = get_datas['save_cookie_path']['save_dir']
    save_filename = get_datas['save_cookie_path']['save_filename']
    # time_stamp=time.strftime('%Y%m%d%H%M%S',time.localtime())
    url='https://work.weixin.qq.com/wework_admin/frame'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    time.sleep(8)
    cookies = driver.get_cookies()
    cookie_save_dir=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),save_dir)
    if not os.path.exists(cookie_save_dir):
        os.mkdir(cookie_save_dir)
    with open(os.path.join(cookie_save_dir,save_filename),'w',encoding='utf-8') as f :
        yaml.safe_dump(cookies,f)

def test_get_cookies(get_yml_datas):
    get_cookies(get_yml_datas)