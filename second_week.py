# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 14:07:37 2025

@author: cic
"""

#조건문
a=200
if a<200:
    print("200보다 작군요")
elif a<100: 
    print("100보다 작군요")
else :
    print("100보다 크군요")


#반복문

print("for loop")
for v in range(10):
    print(v)


print("while loop")
var = 0 
while v<10:
    print(v)
    v+=1
    
print("break/continue")
var = 0 
while v<10:
    print(v)
    v+=1
    if v==5:
        break
