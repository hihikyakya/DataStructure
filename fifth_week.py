#%%

#%%
def arithmetic_sequence(n):
    if n==1:
        return 1
    else:
        return arithmetic_sequence(n-1)+3
def fibonachi_sequence(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibonachi_sequence(n-1)+fibonachi_sequence(n-2)

def hanoi_tower(n,a,b,c):
    if n==1:
        print(f"원반 1을 {a}에서 {b}로 이동")
        return
    hanoi_tower(n-1,a,c,b) #여기 함수 안에서 가장 아래있는 원반을 제외하고 서포트 기둥에 다 옮김
    print(f"원반 {n}을 {a}에서 {b}로 이동") #가장 아래있는 원반을 옮김
    hanoi_tower(n-1,c,b,a) #여기 함수 안에서 서포트 기둥에서 타겟 기둥으로 원반을 다 옮김
        
def selective_sort_recurcive(arr,n=None,index=0,callback=None):
    if n is None:
        n=len(arr)
    
    if index==n:
        return arr
    min_idx=index
    for i in range(index+1,n):
        if callback==None:
            if (arr[i] <arr[min_idx]):
                min_idx=i
        else:
            if callback(arr,i,min_idx):
                min_idx=i
    
    arr[index], arr[min_idx]= arr[min_idx], arr[index]
    
    selective_sort_recurcive(arr,n,index+1)
    

def insert_data(pos,data,m_list):
    a=m_list[:pos+1]
    b=m_list[pos:]
    a.append(data)
    return a+b

def delete_data(pos,m_list):
    n_list=m_list
    del n_list[pos]
    return n_list

#%%
if __name__ == "__main__":
    #재귀함수
    for i in range(1,11):
        print(f"a_{i} =", arithmetic_sequence(i))
    
    #피보나치 수열
    print(f"f_{i} =", fibonachi_sequence(10))
    
    #하노이 탑**
    hanoi_tower(4,"A","B","C")
    
    #선택정렬
    A=[5,2,3,4,6,1,2,3,4,5,6]
    selective_sort_recurcive(A)
    selective_sort_recurcive(A,callback=lambda x,idx,target_idx: x[idx] > x[target_idx])
    print(A)     
    
    #귀납적 사고가 중요하다.
    
    #--------------------
    
    my_list=[1,"$","@!#!@#!@#",False,3.15+1j]
    
    my_list+=["35"]
    print(my_list) #"35"추가, 더 정확히는 배열을 연결한다.(concatenate)
    my_list*=3
    print(my_list) #my_list의 데이터들이 3배로 늘어난다. (repeat)
    
    #list 함수
    my_list2=[]
    my_list2.append(3) #[3]
    my_list2.insert(1,9) #[3,9]
    my_list2.insert(0,45) #[45,3,9]
    my_list2.pop() #[45,3]
    my_list2.pop(0) #[3]
    my_list2.remove(3) #[] 성분 값을 입력해야함. index가 아니라
    my_list2=[3,1,23,4,25,25,]
    my_list2.index(3) #4; my_list2[3]과 같다.
    my_list2.clear() #[]
    my_list2.count(4) #0
    my_list2.extend([3,10,2,4,3,5]) #[3,10,2,4,3,5] l1+l2와 같다.
    copy_list=my_list2.copy() #copy
    reversed_list=copy_list.reverse() #[5,3,4,2,10,3]
    copy_list.sort() #기본적으로 오름차순으로 정렬, [2,3,3,4,5,10]
    
    
    #직접 리스트 함수 만들어보기
    test_list=[10,3,0.5,1j,3]
    test_list=insert_data(2,3,test_list)
    print(test_list)
    test_list=delete_data(0,test_list)
    print(test_list)
    
    
    