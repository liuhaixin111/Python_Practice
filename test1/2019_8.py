a = list(map(int,input().split()))
n = 0
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        n += 1
if n > 1:
    print(0)
else:
    print(1)
