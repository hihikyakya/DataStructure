# -*- coding: utf-8 -*-
#%%라이브러리 파트
##모듈:함수의 집합
#import second_week
#import second_week as sw
from second_week import summation_return_or_not #summation_return_or_not 하나만 갖고 온다.
#from second_week import * #from second_wekk import [ALL]: 해당 모듈의 모든 정의를 들고옵니다.

#외장함수
import sys #와 같이 import를 사용해 호출할 수 있는 모듈: sys는 system의 약자
import os #디렉터리, 파일 조작 모듈
import pickle #파일 저장,작성 모듈
import random #난수 생성함수 <=시뮬레이션시 자주 사용함.
import math #수학 라이브러리
import time #시간관련처리시
import datetime #날짜와 시간 관련 처리

#%%정의 파트

#class
class Counter:
    def __init__(self): #생성자 함수
        self.count=0 #self.count라는 변수는 지역변수이다.
    def increment(self): #추가 동작 함수
        self.count+=1 #self를 사용해서 self에서 count를 불러와서 사용할 수 있다.

class Car:
    def __init__(self,n_wheels,n_windows,n_lights,color="black"):
        #추가 변수들..
        self.n_wheels=n_wheels 
        self.n_windows=n_windows
        self.n_lights=n_lights
        self.velocity=0
        self.color=color
    def move(self):
        self.velocity+=1
    def log_color(self):
        print(self.color)
    
    def change_color():
        color='Yellow'
        print(color)
        


#클래스 실습
class Employee:
    def __init__(self,name,years_from_being_employee,has_degree=False):
        self.name=name
        self.years_from_being_employee=years_from_being_employee
        self.rank=self.get_rank()
        self.annual_salary=self.cal_annual_salary()
        self.has_degree=has_degree
    def print_name_and_annual_salary(self):
        print(self.name)
        if self.has_degree:
            print(str(self.annual_salary+1400)+"만원")
        else:
            print(str(self.annual_salary)+"만원")
    
    def cal_annual_salary(self):
        if self.rank=="사원":
            return 3000+ self.years_from_being_employee*100
        elif self.rank=="대리":
            return 3100+ self.years_from_being_employee*110
        return 4000+ self.years_from_being_employee*130 #단순 return 문에서는 else를 안써도 같은 방향으로 동작합니다.
    
    def get_rank(self):
        if self.years_from_being_employee<=5:
            return "사원"
        elif self.years_from_being_employee<=10:
            return "대리"
        return "과장"

#상속
class HyendaiCar(Car):
    def __init__(self,n_wheels,n_windows,n_lights,color="black"):
        super().__init__(n_wheels, n_windows, n_lights,color)
        
    def move(self): #method overidding
        self.velocity+=2
#%%main body

if __name__ == "__main__":
    x=4
    y=10
    #second_week.summation_return_or_not(x, y)
    #sw.summation_return_or_not(x, y)
    summation_return_or_not(x,y)
    
    ##
    car1 = Car(4,4,4,"blue") #객체 생성
    
    car1.log_color() # 객체에 정의된 내용 사용
    
    Car.change_color()
    
    employee1=Employee("철수",7,True) #철수 회사원 객체 생성
    employee2=Employee("yasuo",1,False) #야스오 회사원 객체 생성
    
    employee1.print_name_and_annual_salary()
    employee2.print_name_and_annual_salary()
    
    #debugging용
    print(employee1.rank)
    print(employee2.rank) 
    
    car2 = HyendaiCar(4, 4, 4, "Black")
    car2.move()
    print(car2.velocity)
    
    ##내장함수:클래스로 구성
    
    print(abs(-x)) #절대값 출력
    
    #list와 불리언
    ###all, any함수
    l=[0,2,3,4]
    bl=[i==0 for i in l]
    print(all(bl))
    print(any(bl))
    
    
    #-------------------
    
    ###zip함수
    l1=[1,2,3,5]
    l2=[5,6,7,2]
    
    zip_iter=zip(l1,l2) #두개 이상의 리스트를 묶어서 인덱스 번호 순서대로 반환
    for a1,a2 in zip_iter: #바로 여기서 zip함수 쓰면됨
        print(a1,"//",a2)
        
    
    ###enumerator함수
    for i, a in enumerate(l1): #인덱스도 필요할때 사용
        print("index:", i)
        print("value:", a)
    
    ###filter함수
    dynamic_list=["assd",1,3.53,False]
    filtered=filter(lambda x: type(x)==int, dynamic_list) #lambda는 잠깐 쓰고 말 함수를 만드는것
    filtered_list=list(filtered)
    print(filtered_list) #integer값만 출력
    
    ###range함수
    gr=range(1,10) #1~9까지의 값 생성
    list_gr=list(gr) #list로 변환
    print(list_gr)
    
    ###list와 range함수
    for i in range(len(l1)): #len과 range함수를 함께 사용
        print(l1[i])
        
        
    ###sort함수=>정렬: 나중에 배움
    
    ###map함수: ex) map함수로 딕셔너리 만들기
    new_dict=dict(map(lambda x: (x,x%2), l1))
    print(new_dict)
    
    ##os모듈
    dirs=os.listdir(os.path.dirname(__file__)) #현재 파일이 있는 위치의 디렉토리에 있는 파일들을 list로 변환
    print(dirs)
    
    ##with문과 pickle모듈
    with open("test file.plk","+wb") as f:
        pickle.dump(dirs, f) #변수를 파일에 저장
        
    ##random함수: 통계에서 주로 사용
    distribution=[]
    for i in range(100):
        distribution.append(random.random())
    
    ##time함수 : 1970년부터 지난초출력
    print(time.time())
    
    
    #***2번째 레포트
    questions=[] #질문 10개
    answers = []
    for i in range(len(questions)):
        answers.append(int(input(questions[random.randint(0,len(questions))]))) #**비복원추출로 수정필요
    
    #채점하기
    
    #파일 저장
    with open("file.db","+wb") as f:
        pickle.dump(f)