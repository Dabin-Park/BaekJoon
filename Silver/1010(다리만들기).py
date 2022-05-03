# 방법 1
a = int(input())

for _ in range(a):
    x,y = map(int, input().split())
    b = 1
    for i in range(x):
        if x == y:
            b = b
        else :
            b *= (y - i)/x
            x -= 1

    print(f"{b:.0f}")
    
# 방법 2    
def factorial(n):
    a = 1
    for i in range(n):
        a *= (n-i)
    return a

A = int(input())

for _ in range(A):
    a,b = map(int,input().split())
    c = factorial(b)//(factorial(b-a)*factorial(a))
    print(f"{c:.0f}")
