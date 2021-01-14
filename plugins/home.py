from robot.sdk.AbstractPlugin import AbstractPlugin

class Plugin(AbstractPlugin):
	SLUG = "AAAA"  

	def prHello(self):
		print("这是一个函数")

	def prHello1(self):
		print("这是一个函数1")

	def prHello2(self):
		print("这是一个函数2")

	def handle(self,query):
		self.say("你好世界")
		print("你好世界")
		self.prHello()
		self.prHello1()
		self.prHello2()
		return 

	def isValid(self,query):
		return any(word in query for word in ["AAA", "AA","BBB","CC"])




