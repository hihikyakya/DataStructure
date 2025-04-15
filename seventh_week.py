#%% modules
#%% definitions
#스택 구현
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity #스택 상자 사이즈
        self.array=[None]*self.capacity #스택공간 생성 이건 무조건 array여야한다.
        self.top=-1
    
    def isEmpty(self):
        return self.top==-1 #초기상태는 비어있다.
    def isFull(self):
        return self.top==self.capacity-1 #capacity-1가 최대주소번지니까 가장 위의 주소번지가 최대주소번지와 같으면 꽉 찬 것이다.
    
    def push(self, e):
        if not self.isFull(): #차있는지 확인하고 넣는다.
            self.top+=1
            self.array[self.top] = e
        else:
            pass #이때 넣으면 오버플로우
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            tmp=self.array[self.top+1]
            del self.array[self.top+1]
            
            #여기 오류있음.
            return tmp
        else:
            pass #이때 빼면 언더플로우
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass
#%% main body
if __name__=="__main__":
    #스택 생성하고 실험해보기
    stack=ArrayStack(10)
    for i in range(5):
        stack.push(i)
        print("넣음")
    print("가득참?",stack.isFull())
    for i in range(3):
        print(stack.peek(),"<=꺼낸값, 삭제는 안함")
    for i in range(3):
        #print(len(stack.array),"디버그용")
        print(stack.pop(),"<=꺼낸값")
    print("비었는가?",stack.isEmpty())
    
    
    #괄호 검사
    txt="(2*3+0.5))"
    stack2=ArrayStack(len(txt))
    
    for t in txt:
        stack2.push(t)
    
    is_vaild=0
    for i in range(stack2.capacity):
        v=stack2.pop()
        if v=="(":
            is_vaild+=1
        elif v==")":
            is_vaild-=1
    
    if is_vaild!=0:
        print("error!")
    else:
        print("success")
    
    
    #문자열 뒤집기
    hi="안녕하세요"
    stack3=ArrayStack(len(hi))
    for h in hi:
        stack3.push(h)
    
    new_hi=""
    for i in range(stack3.capacity):
        new_hi+=stack3.pop()
    
    print(new_hi)
    
    
    #postfix
    postfix="123*+"
    
    stack4=ArrayStack(len(postfix))

    for p in postfix:
        stack4.push(p)
    
    first_value=None
    second_value=None
    operator=None
    
    while(not stack4.isEmpty()):
        for i in range(stack4.capacity):
            v=stack4.pop()
            if v not in "1234567890":
                if operator==None:
                    operator=v
                else:
                    stack4.push(v)
            else:
                if first_value==None and second_value==None:
                    second_value=int(v)
                elif first_value==None:
                    first_value=int(v)
            
            if first_value!=None and second_value!=None and operator!=None:
                print(first_value,operator,second_value)
                if operator=="*":
                    first_value=first_value*second_value
                elif operator=="+":
                    first_value=first_value+second_value
                
                second_value=None
                operator=None
        
    
    print(first_value)
    
    
    
        