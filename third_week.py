# -*- coding: utf-8 -*-
#%%라이브러리 파트
##모듈:함수의 집합
#import second_week
#import second_week as sw
from second_week import summation_return_or_not #summation_return_or_not 하나만 갖고 온다.
#from second_week import * #from second_wekk import [ALL]: 해당 모듈의 모든 정의를 들고옵니다.

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
    l=[0,2,3,4]
    print(all(l))
    print(any(l))
    