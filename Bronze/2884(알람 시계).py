# 2884

A = list(map(int, input().split()))

if A[1]-45 < 0 :
    A[0] = (A[0]-1) % 24
    A[1] +=  15
    print(A[0], A[1])
else :
    A[1] -= 45
    print(A[0], A[1])

# 함수로 하면 좋음 
'''    
def wakeup(H,M):
    if M-45 < 0 :
        H = (H-1) % 24
        M +=  15
    else :
        M -= 45
    return print(H, M)

H, M = list(map(int, input().split()))
wakeup(H,M)
'''    
