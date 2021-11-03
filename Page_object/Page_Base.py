import logging
from Base_class.Base import Keywork
from selenium.webdriver.support import expected_conditions as EC

class Page_Base(Keywork):

	def xx(self,i):
		self.open('https://www.baidu.com/')
		self.input('id','kw',str(i))
		self.click('id','su')
		if EC.url_contains(i)(self.driver):
			logging.info('url存在{}'.format(i))
		else:
			logging.info('url不存在{}'.format(i))