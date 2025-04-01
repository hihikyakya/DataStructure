#%% library
import numpy as np #행렬 연산 모듈
import pandas as pd #데이터 분석 모듈
import matplotlib.pyplot as plt



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
    titanic_df = pd.read_csv("pandas\\titanic.csv") 
    
    ages=titanic_df['Age'] #Age한 줄만
    titanic_df.describe() #최대값, 중위값, 평균 등등 나옴
    
    ##head:상위 데이터 몇개만 확인
    titanic_df.head()
    
    #그외 여러 함수 사용가능..
    
    ##merge함수
    df1=pd.DataFrame({"employee":['Kim','Park'],'age':[10,40]})
    df2=pd.DataFrame({'employee':['Kim','Lee'],'age':[20,15]})
    
    pd.merge(df1,df2)

    ##dropna
    titanic_df.dropna(how='all')
    ##fillna
    titanic_df.fillna(titanic_df['Pclass'].mean())
    
    
    #시각화:Matplotlib
    plt.plot([1,2,3,4,56,67,6,213,213,14,21,32,423,12,3,412,])
    plt.show()
    
    X=[1,2,3,4,3,1,2,5,7,31,2,3]
    Y=[0.1,2,0.5,0.3,0.7,0.8,0.9,1,2,3,4,0.2]
    plt.plot(X,Y,label="Seoul") #**x,y, label지정
    plt.plot(X,np.array(Y)*np.exp(np.array(X)/10),label="Busan") #x,y, label지정
    plt.xlabel('day') #x축
    plt.ylabel('temperature') #y축 
    plt.legend(loc='upper left') #지표설명 위치 지정
    plt.title("temperature") #제목
    plt.show()
    
    
    ##막대그래프 그리기
    X=["Mon","Tue","Web","Thur","Fri","Sat","Sun"]
    Y=[15.6,17.2,16.5,14.3,17.9,11,4]
    plt.bar(list(range(7)),X)
    plt.xticks(list(range(7)),Y)
    plt.show()
    
    ##hist=>히스토그램
    
    ##막대그래프 그리기-pandas df.plot(kind='bar',x='name',y='age')
    
    ##산포도(점들) 그리기-pandas df.plot(kind='scatter', x='children', y='pets',color='red')
    
    
    #-------------------------------여기까지 이해했다면 파이썬 완료
    
    
    
    
    
    
    
    