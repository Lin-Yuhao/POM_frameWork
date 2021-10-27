# -*- coding: utf-8 -*-

import allure
from ddt import *
from Page_object.Page import Page

'''
@allure.severity('用例等级')
blocker：阻塞缺陷(功能未实现，无法下一步)
critical：严重缺陷(功能点缺失)
normal： 一般缺陷(边界情况，格式错误)
minor：次要缺陷(界面错误与ui需求不符)
trivial： 轻微缺陷(必须项无提示，或者提示不规范)
'''


@ddt
@allure.feature('个人信息模块')
class Test_personal:

	@file_data('../Case_date/login.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试登录功能')
	@allure.description('描述')
	@allure.severity('blocker')
	def test_login(self,**kwargs):
		lg = Page()
		lg.login(kwargs['账号'],kwargs['密码'])
		lg.quit(0)

	@file_data('../Case_date/information.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试修改个人信息功能')
	@allure.description('描述')
	def test_information(self,**kwargs):
		im = Page()
		im.information(kwargs['姓名'],kwargs['性别'],kwargs['生日'],
		               kwargs['地区1'],kwargs['地区2'],kwargs['地区3'],
					   kwargs['QQ'],kwargs['旺旺'],kwargs['MSN'],)
		im.quit(0)

	@file_data(r'../Case_date/change_password.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试修改用户密码功能')
	@allure.description('描述')
	def test_change_password(self,**kwargs):
		ld = Page()
		ld.modify_password(kwargs['旧密码'],kwargs['新密码'],kwargs['重复密码'])
		ld.quit(0)

	@file_data('../Case_date/modifyemail.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试修改电子邮件功能')
	@allure.description('描述')
	def test_modify_email(self,**kwargs):
		me = Page()
		me.modify_email(kwargs['密码'],kwargs['邮箱'])
		me.quit(0)

	@file_data(r'../Case_date/modify_number.yaml')
	@allure.step(title="参数与截图")
	@allure.title(test_title='测试修改手机号码功能')
	@allure.description('描述')
	def test_modify_number(self,**kwargs):
		mu = Page()
		mu.modify_number(kwargs['手机号'])
		mu.quit(0)
