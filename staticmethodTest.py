class StaticMethodTesting(object):
	def __init__(self):
		self.val = "Hello World!"
	@staticmethod
	def testNumber(arg):
		return isinstance(arg, int)
obj = StaticMethodTesting()
print(obj.testNumber('kunal'))