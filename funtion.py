'''
DATE:17TH DEC 2022
DAY: SATURDAY
TOPIC: FUNTION
AUTHOR:RAMA BHARGAvi
'''
def greet():
    print('Hello')
greet()
def greet(n):
    print('Hello '+str(n))
greet(6)
greet('PY')
def greet(*names):
    print('Hey',names[-1])
greet('python','programming','core','functions')
def details(n,a):
    print('Hey '+n + ' ! your age is '+str(a))
details('hd',25)
details(n='HD',a=26)
details(a=26,n='HD')
def details(n,a):
    print('Hey '+n + ' ! your age is '+str(a))
n=input('Enter ypur name: ')
a=input('Enter your age: ')
details(n,a)
def r(x,y):
    return x*y
print(r(5,6))
