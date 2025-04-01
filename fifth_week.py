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
    hanoi_tower(n-1,a,c,b)
    print(f"원반 {n}을 {a}에서 {b}로 이동")
    hanoi_tower(n-1,c,b,a)
        
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
    
    #귀납적 사고