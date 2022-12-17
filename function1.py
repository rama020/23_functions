'''
DATE:17TH DEC 2022
DAY: SATURDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
'''
def gm():
    '''Author: Python
    the time is now 9:35
we are doing function topic'''
print(gm.__doc__)
def into(name="HEY",age=45):
    print('name :',name)
    print('age :',age)
into()
into('py')
into('ravi',25)
into(name='gopal')
into(age=26)
def s(a,b):
    c=a+b
    d=a+b
    print('sum is',c)
    print('sum is',d)

s(10,20)
s(10.5,2.3)
def sum(a,b):
    c=a+b
    return c  

x=sum(10,20) 
print('sum is',x)
y=sum(10.5,2.3) 
print('sum is:',y)  