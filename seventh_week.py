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
            self.array[self.top+1]=None #del사용시는 array length도 줄어서 코드가 다 꼬임. stack은 고정크기 배열을 사용한다는 것을 주의하자.
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
    postfix="9472/*+" #((7/2)*4)+9
    
    stack4=ArrayStack(len(postfix))

    #연산방법: 숫자인경우 push, 연산자인경우에 pop 2번해서 계산
    first_value=None
    second_value=None
    for p in postfix:
        if p in "1234567890":
            stack4.push(int(p))
        else:
            second_value=stack4.pop()
            first_value=stack4.pop()
            if p=="*":
                stack4.push(first_value*second_value)   
            elif p=="-":
                stack4.push(first_value-second_value)   
            elif p=="+":
                stack4.push(first_value+second_value)   
            elif p=="/":
                stack4.push(first_value/second_value)  
        print(stack4.peek())
    print(stack4.pop())
    
        