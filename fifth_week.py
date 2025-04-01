#%%

#%%
def arithmetic_sequence(n):
    if n==1:
        return 1
    else:
        return arithmetic_sequence(n-1)+3
#%%
if __name__ == "__main__":
    #재귀함수
    for i in range(1,11):
        print(f"a_{i} =", arithmetic_sequence(i))