# 4344

a = int(input())    # 케이스 개수
t = []

for _ in range(a):
    n = 0
    s = list(map(int, input().split())) # 학생수,각각 점수
    m = sum(s[1:])/s[0] # 평균
    for i in range(len(s)-1):
        if s[i+1] > m :
            n += 1
    t.append(n/s[0]* 100)
            
for i in range(len(t)):
        print(f"{t[i]:.3f}%")

'''
a = int(input())    # 케이스 개수

for _ in range(a):
    n = 0
    s = list(map(int, input().split())) # 학생수,각각 점수
    m = sum(s[1:])/s[0] # 평균
    for i in range(len(s)-1):
        if s[i+1] > m :
            n += 1
    print(f"{n/s[0]*100:.3f}%")
'''
        

