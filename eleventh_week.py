#%% import section

#%% def section
class ArrayStack:
    def __init__(self,array_size):
        self.array_size=array_size
        self.space=[-1]*array_size
        self.top=-1
        
    def is_full(self):
        return self.array_size==self.top+1
    def is_empty(self):
        return self.top==-1
    def push(self,x,pushpop=False):
        if self.is_full():
            raise IndexError("가득 차서 더 넣을 수 없습니다.")
        self.space[self.top+1]=x
        self.top+=1
        if pushpop:
            self.pop()
    def pop(self):
        if self.is_empty():
            raise IndexError("값을 꺼낼 수 없습니다.")
        temp=self.space[self.top]
        self.space[self.top]=-1
        self.top-=1
        return temp
    def peek(self):
        if self.is_empty():
            raise IndexError("값을 꺼낼 수 없습니다.")
        return self.space[self.top]
    def size(self):
        return self.top+1
#%% main body
if __name__=="__main__":
    pass