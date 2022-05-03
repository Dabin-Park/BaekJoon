# 2609 

A = list(map(int, input().split()))

a = max(A[0], A[1])
b = min(A[0], A[1])

    
while True :
    if b == 0 :
        print(a) 
        print((A[0]*A[1])//a) 
        break;
    elif a % b == 0 :
        print(b)
        print((A[0]*A[1])//b) 
        break;
    elif a > b : 
        a %= b
    else :
        b %= a    

            

    


    
