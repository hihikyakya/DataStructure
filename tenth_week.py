#%% import section
#%% def. section
class ArrayList:
    def __init__(self):
        self.list=[]
    def append(self,x)->None:
        self.list+=[x];
    def pop(self,i):
        if len(self.list)==0:
            raise IndexError("삭제가능한 요소가 없습니다.")
        
        temp=self.list[i]
        del self.list[i]
        
        print(temp)
        
        return temp
    def remove(self, x):
        if len(self.list)==0:
            raise IndexError("삭제가능한 요소가 없습니다.")
        for i,a in enumerate(self.list):
            if a==x:
                del self.list[i]
                return
        raise Exception("같은 요소가 없어요.")
    def index(self, x):
        if len(self.list)==0:
            raise IndexError("빈 리스트")
        for i,a in enumerate(self.list):
            if a==x:
                return i
        raise Exception("같은 요소가 없어요.")
    def extend(self, a):
        if len(a)==0:
            raise IndexError("빈 iterable 요소")
        for _x in a:
            self.append(_x)
    def clear(self):
        self.list=[]
    def count(self,x):
        count=0
        for i,a in enumerate(self.list):
            if a==x:
                count+=1
        return count
    def copy(self):
        new_list=ArrayList()
        for a in self.list:
            new_list.append(a)
        return new_list
    def reverse(self):
        new_list=[]
        for i in range(len(self.list)):
            new_list.append(self.list[len(self.list)-i-1])
        self.list=new_list
        
class ArrayStack:
    def __init__(self,size):
        self.size=size
        self.space=[-1]*size
        self.top=-1
        
    def full(self):
        return self.size==self.top+1
    def empty(self):
        return self.top==-1
    def push(self,x):
        if self.full():
            raise IndexError("가득 차서 더 넣을 수 없습니다.")
        self.space[self.top+1]=x
        self.top+=1
    def pop(self):
        if self.empty():
            raise IndexError("값을 꺼낼 수 없습니다.")
        temp=self.space[self.top]
        del self.space[self.top]
        self.top-=1
        return temp
    def peek(self):
        if self.empty():
            raise IndexError("값을 꺼낼 수 없습니다.")
        return self.space[self.top]
    def size(self):
        return self.top+1

class Game:
    def __init__(self,n_players):
        self.n_players=n_players
        self.history=ArrayList()
    def is_short_word(self, word):
        return len(word)==1
        
    def run(self):
        prev_word=''
        flag=1
        while flag==1: #순환
            for i_p in range(self.n_players):
                ith_word=input(f"{i_p+1}번째 사람의 단어: ")
                while self.is_short_word(ith_word) or (ith_word in self.history.list):
                    ith_word=input(f"다시 입력 {i_p+1}번째 사람의 단어: ")
                if prev_word!='' and prev_word[-1]!=ith_word[0]:
                    flag=0
                    return i_p+1 #종료
                prev_word=ith_word
                self.history.append(ith_word)
#%% main body
if __name__=="__main__":
    arrayList=ArrayList()
    arrayList.append(1)
    print(arrayList.list)
    arrayList.append(2)
    arrayList.append(3)
    arrayList.append(4)
    arrayList.reverse()
    print(arrayList.list)
    arrayList2=arrayList.copy()
    arrayList2.list[0]=100000
    print(arrayList2.list)
    print(arrayList.list)
    
    game=Game(2)
    print("진사람:",game.run())