import time
import pytest
from page_objects.login_page import Login_Page

class TestCases:
    def setup_class(self):
        self.home = Login_Page().login("manage","manage123")

    def teardown_class(self):
    #     time.sleep(5)
        self.home.do_quit()

    @pytest.mark.parametrize('catagory_name',['a','b'])
    def test_add(self,catagory_name):
        time.sleep(3)
        res = self.home\
            .goto_category_page()\
            .go_add_page()\
            .add_category(catagory_name)\
            .get_add_result()
        assert res == "创建成功"

        # assert self.category_page.check_element_exist() != []

    @pytest.mark.parametrize('catagory_name', ['da','db'])
    def test_delete(self,catagory_name):
        time.sleep(3)
        res = self.home \
            .goto_category_page() \
            .go_add_page() \
            .add_category(catagory_name) \
            .delete_category(catagory_name)\
            .get_delete_result()
        assert res == "删除成功"
        # assert self.category_page.check_element_exist() == []
if __name__ == '__main__':
    #为什么这样写还是跑的整改文件中的用例？？？
    pytest.main(['liter_testcases.py::TestCases::test_delete','-vs'])