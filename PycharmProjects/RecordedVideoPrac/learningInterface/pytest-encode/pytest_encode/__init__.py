from typing import List
import pytest


def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
	print(items)
	for item in items:
		#用例的名字
		# print(item.name)
		item.name = item.name.encode('utf-8').decode('unicode-escape')
		#用例的路径
		# print(item._nodeid)
		item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
	# 	if 'departmentList' in item.name:
	# 		item.add_marker(pytest.mark.getlist)
	# items.reverse()