# -*- coding: utf-8 -*-

import allure
from ddt import *
from Page_object.Page import Page

@ddt
@allure.feature('模块名')
class Test_xx:

	@file_data('../Case_date/login.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试某功能')
	@allure.description('描述')
	@allure.severity('blocker')
	def test_xx(self,**kwargs):
		lg = Page()
		lg.xx(kwargs['内容'])
		lg.quit(1)