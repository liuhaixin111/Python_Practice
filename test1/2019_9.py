n = int(input())
temp = list(map(int,input().split()))
sum = 0
for i in temp:
    sum += i-1
print(sum)