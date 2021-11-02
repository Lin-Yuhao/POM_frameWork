from Base_class.Base import Keywork


class Page_Base(Keywork):

	def login(self,i):
		self.open('https://www.baidu.com/')
		self.input('id','kw',str(i))
		self.click('id','su')