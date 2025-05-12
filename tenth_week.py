#%% import section
#%% def. section
class ArrayList:
    def __init__(self):
        self.list=[]
    def append(self,x)->None:
        self.list+=[x];
    def pop(self,i):
        temp=self.list[i]
        del self.list[i]
        return temp
    def remove(self, x):
        for i,a in enumerate(self.list):
            if a==x:
                del self.list[i]
    def index(self, x):
        for i,a in enumerate(self.list):
            if a==x:
                return i
    def extend(self, a):
        for _x in a:
            self.append(_x)
    def clear(self):
        self.list=[]
    def count(self,x):
        count=0
        for i,a in enumerate(self.list):
            if a==x:
                count+=1
        return count
    def copy(self):
        new_list=ArrayList()
        for a in self.list:
            new_list.append(a)
        return new_list
    def reverse(self):
        new_list=[]
        for i in range(len(self.list)):
            new_list.append(self.list[len(self.list)-i-1])
        self.list=new_list
#%% main body
if __name__=="__main__":
    arrayList=ArrayList()
    arrayList.append(1)
    print(arrayList.list)
    arrayList.append(2)
    arrayList.append(3)
    arrayList.append(4)
    arrayList.reverse()
    print(arrayList.list)