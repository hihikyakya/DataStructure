#%% library
import numpy as np #행렬 연산 모듈

import pandas as pd #데이터 분석 모듈


#%% def.


#%% main.
if __name__=="__main__":
    #numpy
    arr1= np.array([1,2,46,1,4,21]) #배열 생성
    
    ##배열 계산
    arr1_4=arr1+4 
    arr2=np.array([5,2,1,0.2,4,7])
    arr3=arr1+arr2
    
    arr3 = arr1@arr2.T #또는 arr2.transpose()
    
    
    ##직접해보기: BMI지수 계산
    heights=np.array([1.83,1.76,1.69,1.86,1.77,1.73])
    weights=np.array([86,74,59,95,80,68])

    BMI=weights/(heights**2) #요소곱과 행렬곱을 헷갈리지 맙시다.
    print(f"사람 {heights.shape[0]}명의 BMI지수는 다음과 같습니다....",*np.round(BMI,3),"(kg/m^2)")
    
    ##np.arange와 np.linspace
    np.arange(1,10,1) #step
    np.linspace(1,10,100) #slice
    
    np.random.seed(100) #random seed설정
    
    ##평균
    mean1=np.mean(arr1, axis=0) #행에 대한 평균
    mean0 = np.mean(arr1, axis=None) #전체 평균
    
    ##MSE
    data=np.array([0,0,0,1,1])
    x=np.array([0,1,1,0,1])
    MSE_value = np.mean((x-data)**2)
    print(MSE_value)
    
    
    #pandas
    titanic = pd.read_csv("pandas\\titanic.csv") 
    