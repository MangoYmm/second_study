import threading
import time

import pytest

from test_pytest.api.tag import Tag
from test_pytest.tests.test_tag import fake

@pytest.fixture()
def get_unique_name():
    # threading.currentThread.__name__获取线程的名字
    # 这样就解决了并行的时候时间戳相同的情况
    name = fake.name()
    tag_name = name+str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + threading.currentThread().name
    return tag_name
@pytest.fixture()
def get_new_tagid(get_unique_name):
    r=Tag().add(get_unique_name).json()
    tag_id=r.get("tagid")
    # for i in Tag().get().json().get("taglist"):
    #     if i["tagid"]==tag_id:
    #         tagname=i["tagname"]
    # print(tag_id,tagname)
    return tag_id

# def test_a(get_unique_name):
#     print(get_new_tagid(get_unique_name))