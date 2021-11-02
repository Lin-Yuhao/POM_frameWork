from Page_object.Page_Base import Page_Base
import logging


class Page(Page_Base):

	def login(self,usr,pwd):
		self.c_login(usr,pwd)
		self.v_url("http://120.55.190.222:8083/user/login.htm",
		           "http://120.55.190.222:8083/user_login_success.htm",
		           "http://120.55.190.222:8083/login_error.htm")

	def information(self,name,Gender,bday,region1,region2,region3,QQ,WW,MSN):
		self.c_lppersonal_data()
		self.input('xpath','//*[@id="trueName"]',name)
		self.cld("birthday",bday)

		if Gender=='男':
			self.click('xpath','//*[@id="theForm"]/table/tbody/tr[8]/td[2]/label[2]/input')
		elif Gender=='女':
			self.click('xpath','//*[@id="theForm"]/table/tbody/tr[8]/td[2]/label[3]/input')
		elif Gender=='保密':
			self.click('xpath','//*[@id="theForm"]/table/tbody/tr[8]/td[2]/label[1]/input')
		elif Gender !='男'or'女'or'保密' :
			logging.info('输入值没有这个选择，略过选择性别')

		self.down('xpath','//*[@id="areas_province"]',region1)
		self.down('xpath', '//*[@id="areas_city"]', region2)
		self.down('xpath', '//*[@id="area_id"]', region3)

		self.input('xpath','//*[@id="QQ"]',QQ)
		self.input('xpath','//*[@id="WW"]',WW)
		self.input('xpath','//*[@id="MSN"]',MSN)
		self.click('xpath','//*[@id="theForm"]/table/tbody/tr[14]/td[2]/span/input')

		self.v_url('http://120.55.190.222:8083/buyer/account.htm',
				   'http://120.55.190.222:8083/buyer/account_save.htm',
				   '')

	def modify_password(self,pwd,npwd,dpwd):
		self.c_lppersonal_data()
		self.click('xpath','//*[@id="centerbg"]/div[2]/div[1]/ul/li[2]/a')
		self.input('xpath','//*[@id="old_password"]',pwd)
		self.input('xpath','//*[@id="new_password"]',npwd)
		self.input('xpath','//*[@id="new_password1"]',dpwd)
		self.click('xpath','//*[@id="theForm"]/table/tbody/tr[4]/td[2]/span/input')
		self.v_url('http://120.55.190.222:8083/buyer/account_password.htm',
		           'http://120.55.190.222:8083/buyer/account_password_save.htm',
		           '')

	def modify_email(self,pwd,email):
		self.c_lppersonal_data()
		self.click('xpath','//*[@id="centerbg"]/div[2]/div[1]/ul/li[3]/a')
		self.input('xpath','//*[@id="password"]',pwd)
		self.input('xpath','//*[@id="email"]',email)
		self.click('xpath','//*[@id="theForm"]/table/tbody/tr[3]/td[2]/span/input')
		self.v_url('http://120.55.190.222:8083/buyer/account_email.htm',
		           'http://120.55.190.222:8083/buyer/account_email_save.htm',
		           '')

	def modify_number(self,number):
		self.c_lppersonal_data()
		self.click('xpath','//*[@id="centerbg"]/div[2]/div[1]/ul/li[4]/a')
		self.input('xpath','//*[@id="mobile"]',number)
		self.click('xpath','//*[@id="mobile_verify_code_generic"]')
		self.alert(1)
		self.click('xpath','//*[@id="theForm"]/table/tbody/tr[3]/td[2]/span')