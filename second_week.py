# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:07:37 2025

@author: cic
"""

#조건문
print("\nif문")
a=200
if a<200:
    print("200보다 작군요")
elif a<100: 
    print("100보다 작군요")
else :
    print("100보다 크군요")


#반복문

print("\nfor loop")
for v in range(10):
    print(v)


print("\nwhile loop")
var = 0 
while v<10:
    print(v)
    v+=1
    
print("\nbreak/continue")
v = 0 
while v<10:
    print(v)
    v+=1
    if v==5:
        break

#0~9까지 출력하는데 3까지 continue, 7에 break
print("\n문제1:")

v=0
while v < 10:
    if v == 3:
        v+=1 #**while문은 증가시켜줘야한다.
        continue
    elif v == 7 :
        break
    print(v)
    v+=1

print("-->for문으로 변환")

for i in range(10):
    if i == 3:
        continue
    elif i==7:
        break
    print(i)
    
    
print("\nlist")

my_list=[0,1,2,3,4,5,6,7,8,9]

'''다른방법(수업시간에 안 배움, 사용금지, generator)
my_list=[v for v in range(10)]'''

print("\nfor문과 append를 사용하여 list값 생성")
my_list2 = []
for i in range(100):
    my_list2.append(0)

my_list2.pop() #뒤쪽 값 제거
my_list2.pop(0) #0번째 값 제거
my_list2.sort() #특정기준으로 정렬
my_list2.index(0,0,len(my_list2)) #값 찾아보기

#index로 값 찾기
print(my_list2[2]) #왼쪽에서 3번째값
print(my_list2[:]) #원래배열과 같다. 처음부터 끝까지
print(my_list2[3:]) #3번부터 끝까지
print(my_list2[:len(my_list)-1]) #처음부터 마지막 전까지
print(my_list2[1:len(my_list)-3]) #1번째부터 마지막에서 3번째 전까지

print("\n다차원 리스트") #리스트속의 리스트
my_mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
    ] #3,4 shape data

my_img = [
    [
     [3],
     [4],
     [5],
     [6]
     ],
    [
     [1],
     [2],
     [5],
     [6]
     ],
    [
     [7],
     [8],
     [1],
     [3]
     ]
    ] #3,4,1 shape data
print("\n for문 이용")
my_img2 = []
for i in range(3):
    channel_list=[]
    for j in range(4):
        height_list=[]
        for k in range(1):
            height_list.append(k)
        channel_list.append(height_list)
    my_img2.append(channel_list)
            
print("my image",my_img)
print("my image2",my_img2)

print("\ndictionary")
key="안녕"
value = "hi"
my_dict = {key:value}

print("\nset")
my_set={1,2,3,4,5} #집합 연산시에 자주 씁니다. 유니크한 값들을 뽑을때 사용함

print("\ntuple")
my_value = (10) #그냥 10입니다.
my_tuple1 = (10,) #1개짜리 값 tuple, 인수로 튜플을 넣어야 동작할때 사용한다.
my_tuple2 = (10,3,4) #3개짜리 튜플
my_tuple2[0] #인덱싱가능


#------------------------


#%%함수(function)

#return이 있는 함수 형식
##인수가 없는 함수 형식
def my_process():
    return 10

##인수가 있는 함수 형식
def func(*args,**kwargs):
    something = my_process();
    return something

#return이 없는 함수
##인수가 없는
def void_func():
    print("this is void function")
#인수가 있는
def print_summation(x,y):
    print(x+y)


#%%주석으로 세션 나누는법 : #%%사용

#레포트 작성시 #%%을 사용하여 다음과 같이 나눕니다. (예시)

#%% import

import numpy as np


#%% definitions classes

def my_sum(x,y):
    return x+y

#%% main body

if __name__=="__main__":
    ##변수 선언 <-이렇게 하면 값을 쉽게 변경할 수 있습니다.
    x=1
    y=2
    
    ##process1
    print(my_sum(x,y))
    print(my_sum(y,x))
    
    




