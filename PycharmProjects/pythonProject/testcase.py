import unittest

class TestDemo2(unittest.TestCase):
    def setUp(self) -> None:
        print("每条用例执行前>>>>>>>执行")
    def tearDown(self) -> None:
        print("每条用例执行后>>>>>>>执行")
    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("这个类的用例开始执行前执行")
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("这个类的所有用例执行后执行")
    def testDemo21(self):
        print("第一条用例testDemo21---->执行")
        self.assertEqual(1, 1, msg='msg什么场景下显示')
    def testDemo22(self):
        print("第二条用例testDemo22--->执行")
        self.assertNotEqual(1, 2, msg='msg什么场景下显示')