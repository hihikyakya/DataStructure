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

#%% main body
if __name__=="__main__":
	webBrowser=WebBrowser(ArrayStack(255))
	webBrowser.run()
