class ArrayStack:
	def __init__(self, max_size, array_stack:list|None=None):
		self.max_size=max_size
		if array_stack!=None:
			self.array=array_stack[-self.max_size:]
			for i in range(self.max_size):
				if self.array[self.max_size-1-i]!=None:
					self.top=self.max_size-2-i 
					break
		else:
			self.array=[None]*self.max_size
			self.top=-1
	
	def push(self,e)->bool:
		if self.is_full():
			#raise  IndexError("더 못 넣음")
			return False
		self.array[self.top+1]=e 
		self.top+=1
		return True
	
	def pop(self, init=True):
		if self.is_empty():
			raise IndexError("더 못 꺼냄")
		temp=self.array[self.top]
		if init:
			self.array[self.top]=None 
		self.top=-1
		return temp
	def peek(self):
		if self.is_empty():
			raise IndexError("더 못 꺼냄")
		return self.array[self.top]
	
	def size(self)->int:
		return self.top+1
	def is_empty(self)->bool:
		return self.top==-1
	def is_full(self)->bool:
		return self.top+1==self.max_size
		
	def is_overflow(self):
		return self.top+1>=self.max_size
	def is_underflow(self):
		return self.top<=-