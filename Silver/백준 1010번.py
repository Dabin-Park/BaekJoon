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
    
    

