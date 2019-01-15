class windows:
	__windows_number=0
	__pin=0
	__windows_content=[]
	def load(self,window):
		self.__windows_number+=1
		window.order=self.__windows_number
		self.__windows_content.append(window)
	def next(self):
		for i in range(self.__windows_number):
			self.__windows_content[i].forward()
	def back(self):
		for i in range(self.__windows_number):
			self.__windows_content[i].backward()
	def forward(self):
		self.order-=1
		if self.order==0:
			print('showing %s' % self.windowstype)
	def backward(self):
		self.order+=1
		if self.order==0:
			print('showing %s' % self.windowstype)
class welcoming(windows):
	order=0
	windowstype='welcoming'
class confirming(windows):
	order=0
	windowstype='confirming'
class choosing(windows):
	order=0
	windowstype='choosing'
