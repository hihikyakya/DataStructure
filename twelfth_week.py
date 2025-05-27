#%% import section
from ArrayStack import ArrayStack
#%% def section
class WebBrowser:
	def __init__(self, arrayStack=None):
		self.flag=1
		if arrayStack!=None:
			self.arrayStack=arrayStack
		else:
			self.arrayStack=ArrayStack(255)
		#홈페이지 push
		self.arrayStack.push("$Home")
	def visit(self,url):
		self.arrayStack.push(url)
	def back(self):
		if self.arrayStack.peek()=="$Home" and self.top==0:
			print("더 이상 뒤로 갈 수 없습니다.")
			return
		self.arrayStack.pop(init=False)
	def exit_(self):
		self.flag=0
	def run(self):
		self.flag=1 #**여러번 시행할 경우를 대비해서 처음에 1이라고 설정해줘야함. 
		while(self.flag!=0):
			command=input("명령어 입력>>")
			if "visit" in command:
				visit, page_name = command.split()
				if visit=="visit":
					self.visit(page_name)
				else:
					print("잘못된 명령어")
					
			elif "back"==command:
				self.back()
			elif "exit"==command:
				self.exit_()
			else:
				print("잘못된 명령어")
				continue
			print("현재 페이지:", self.arrayStack.peek())
            

##linear queue
class Queue:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.front=0
        self.back=0
        self.capacity=capacity
    def enqueue(self,e):
        if self.isFull():
            raise Exception("꽉차서 더 못 넣음")
        self.queue[self.back]=e
        self.back+=1
    def dequeue(self):
        if self.isEmpty():
            raise Exception("비어서 더 못 꺼냄")
        temp=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        if self.isEmpty():
            self.front=0
            self.back=0
            self.queue=[]
        return temp
    def isEmpty(self):
        return self.front==self.back
    def isFull(self):
        return self.back+1==self.capacity
    def peek(self):
        if self.isEmpty():
            raise Exception("비어서 더 못 꺼냄")
        return self.queue[self.front]
    def size(self):
        return self.back+1
    
##circular queue
class CircularQueue:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        self.front=0
        self.rear=0
        self.capacity=capacity
    def enqueue(self,e):
        if self.isFull():
            raise Exception("꽉차서 더 못 넣음")
        self.queue[self.rear]=e
        self.rear=(self.rear+1) % self.capacity
    def dequeue(self):
        if self.isEmpty():
            raise Exception("비어서 더 못 꺼냄")
        temp=self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1) % self.capacity
        return temp
    def isEmpty(self):
        return self.front==self.rear
    def isFull(self):
        return self.front==(self.rear+1) % self.capacity
    def peek(self):
        if self.isEmpty():
            raise Exception("비어서 더 못 꺼냄")
        return self.queue[self.front]
    def size(self):
        return (self.rear+1)

#%% main body
if __name__=="__main__":
	# webBrowser=WebBrowser(ArrayStack(255))
	# webBrowser.run()
    queue=CircularQueue(10)
    queue.enqueue(10)
    print(queue.queue)
    queue.enqueue(12)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.enqueue(1)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    print(queue.front)
    print(queue.rear)
    queue.dequeue()
    print(queue.queue)
    print(queue.isEmpty())
    print(queue.front)
    print(queue.rear)
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)