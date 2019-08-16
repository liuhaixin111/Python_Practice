n = int(input())
sum = 1+n+n*(n-1)/2
if n < 2:
    print(None)
elif n == 2:
    print(4)
else:
    print(int(sum))