from  Base_class.Base import Keywork


class Page_Base(Keywork):

	def c_login(self,usr,pwd):
		self.open('http://120.55.190.222:8083/user/login.htm')
		self.input('xpath', '//*[@id="username"]', usr)
		self.input('xpath', '//*[@id="password"]', pwd)
		self.click('xpath', '//*[@id="theForm"]/li[4]/input')

	def c_lppersonal_data(self):
		self.c_login('552144918','yuhao123')
		self.click('xpath', '//*[@id="site-nav"]/ul/li[1]/div/a')
		self.remain('xpath', '//*[@id="SearchForm"]/div/div[2]/ul/li[5]/em/a')
		self.click('xpath', '//*[@id="SearchForm"]/div/div[2]/ul/li[5]/div/div/span[1]/a')