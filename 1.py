a=0
b=0
c=0
def f(a,b,c):
    print("Введите три числа:")
    a=int(input())
    b=int(input())
    c=int(input())
    
    if a>0:
        print(max(a,b,c))
        #return max(a,b,c)
    else:
        print('Результат: ',-1)
a=f(a,b,c)
