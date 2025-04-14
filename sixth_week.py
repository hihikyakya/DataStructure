#%% import section

#%% definition section
class Node:
    def __init__(self,value,index,link=None):
        self.value=value
        self.index=index
        self.prev_link=None #양방향
        self.link=link

#개발중..
class LinkedList:
    def __init__(self,start_node=None):
        self.node=start_node
        self.length=0
        if self.node!=None:
            self.length=1
        
    
    
    def append(self, a):
        if self.node==None:
            self.node=Node(a,self.length,None)
        else:
            node=self.node
            while(node.link!=None):
                node=node.link
            node.link=Node(a,self.length,None)
        self.length+=1
    
    def prev_link(self):
        if self.node.prev_link!=None:
            self.node=self.node.prev_link
            return self
        else:
            print("실패, 이전 값이 없습니다.")
    def next_link(self):
        if self.node.link!=None:
            self.node=self.node.link
            self.node.prev_link=self.node
            return self
        else:
            print("실패, 다음 값이 없습니다.")
    
    def at(self,index):
        if index>=self.length:
            raise IndexError("인덱스 초과")
        node=self.node
        for i in range(self.length):
            if node.index==index:
                return node.value
            node=node.link
    
    def __len__(self):
        return self.length
#%% main body
if __name__=="__main__":
    #aa=[]와 aa[]의 차이점=>대입연산자, =[]은 리스트 값으로 부여, aa[]는 인덱스 연산자
    
    #list와 다항식
    x=2
    pxVar=7*x**3-4*x**2+0*x**1+5*x**0 #하나의 데이터에 많이 저장하는 방식
    ps=[7,-4,0,5] #주소값과 개수만 갖고 있음=>메모리를 적게 차지하는 방식
    
    #다항식 print해보기
    string_px=""
    for p in ps:
        string_px+=f"+{p}x^{len(ps)-1}"
    print(string_px)
    
    #다항식 값 계산
    px_value=0
    for i,p in enumerate(ps):
        px_value+=p*(x**(len(ps)-i-1))
    print(pxVar,"==",px_value)
    
    #교수님의 방법
    ps.reverse() #리스트를 뒤집음 ->None
    px_value=0
    x=3
    for i in range(len(ps)):
        px_value+=ps[i]*x**i
    print(px_value)
    
    #연결 리스트 linked list <=처음값을 알면 다음값도 알 수 있다. == 처음값을 바탕으로 모든 값을 알 수 있다.
    linked_list=LinkedList()
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(10)
    print(linked_list.at(2))
    
    print(linked_list.next_link().prev_link().next_link().node.value)
    
    #-----------------
    
    