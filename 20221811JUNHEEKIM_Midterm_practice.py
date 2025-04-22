#%% module section

#%% definition section
#decimal2binary
def decimal2binary(num):
    #이진법을 입력받을 list만들기
    binary_nums=[]
    #->
    #num//2!=1인가?
    binary_nums.append(num%2)
    while(num//2!=0):
        num=num//2
        binary_nums.append(num%2)
    
    #->
    #binary_nums.reverse()
    binary_nums.reverse()
    #->
    return binary_nums

#binary2decimal
def binary2decimal(binary_nums):
    decimal=0
    for i,b in enumerate(binary_nums):
        decimal+=b*(2**(len(binary_nums)-i-1))
    return decimal
#%% main body
if __name__=="__main__":
    #start->
    #수 25를 입력받는다.
    num=25
    orig_num=25
    #->
    #decimal2binary
    binary_nums=decimal2binary(num)
    #->
    #이진법 결과 출력
    for b in binary_nums:
        print(b,end="")
    #->
    #다시 10진법 체계로 만든뒤
    reconstructed_decimal=binary2decimal(binary_nums)
    #->
    #orig_num==reconstructed_decimal인가?
    if orig_num==reconstructed_decimal:
        print("\n네")
    else:
        print("\n아니오")
    
    #->end