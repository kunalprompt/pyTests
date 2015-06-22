class TestingClassmethod(object):
	def __init__(self):
		self.val = 10
	@classmethod
	def testmethod(cls, value):
		cls.val = value
		return cls
c = TestingClassmethod()
print(c, c.val)
a = TestingClassmethod.testmethod('kunal')
print(a,a.val)

# Reference
# http://stackoverflow.com/questions/12179271/python-classmethod-and-static\
# method-for-beginner?lq=1