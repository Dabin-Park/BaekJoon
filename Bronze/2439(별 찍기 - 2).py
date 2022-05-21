# 2439

n = int(input())  # 몇줄

for i in range(n):
    print(f"{str('*'*(i+1)).rjust(n)}")
    
    
# 위에 처럼 하면 시간이 오래 걸림 (함수를 사용 해서)    
# for i in range(n):
#    print(" "*(n-i-1) + "*"*(i+1)) 
