#school project
from abc import ABC ,abstractclassmethod
class person(ABC):
    def __init__(self,name,id,age,gender,address):
        self.name=name
        self.id=id
        self.age=age
        self.gender=gender
        self.address=address
    @abstractclassmethod
    def info(self):
        return f'name : {self.name}, id: {self.id}, age:{self.age}, gender:{self.gender}, address: {self.address}'
    def set_name(self,name):
        if type(name) == str:
            self.name=name
    def get_name(Self):
        return str(Self.name)
    def set_id(self,id):
        if type(id)==int:
            self.id=id
    def get_id(Self):
        return str(Self.id)
    def set_age(self,age):
        if type(age)==int and age>0:
            self.age=age
    def set_gender(self,gender):
        if type(gender)==str and (gender=='male' or gender=="female"):
            self.gender=gender
    def set_address(self,address):
        self.address=address

class student(person):
    def __init__(self,name,id,age,gender,address,level,grades):
        super().__init__(name,id,age,gender,address)
        self.level=level
        self.grades=grades
    def __getitem__(self,key):
        return self.grades[key]
    def info(self):
        return f'name: {self.name}, id:{self.id}, gender{self.gender},address : {self.address},age:{self.age},level: {self.level},grades :{self.grades}'
    def state(self):
        if sum(self.grades.values())>=100:
            return f'pass'
        else:
            return f'not pass'
class teachers(person):
    def __init__(self,name,id,address,gender,age,subject,salary):
        super().__init__(name,id,address,gender,age)
        self.subject=subject
        self.salary=salary
    def info(self):
        return f'name : {self.name}, id: {self.id}, age:{self.age}, gender:{self.gender}, address: {self.address},subject : {self.subject},salary: {self.salary}'
    def s_per_m(self,hours):
        self.salary=hours*200
    
kareem=student(name='kareem',id=222102535,age=22,gender="male",address="maadi",level=2,grades={"math":30,"bio":45,"arabic":45,"english":47})
ahmed=teachers(name="ahemd",id=544,age=55,address="helwan",gender="male",subject="arabic",salary=3000)

            
                



    
        


    
    
    
    