n = int(input())
ans = ''
sum = 0
if n == 0:
    ans = '0'
elif n == 1:
    ans = '01'
else:
    while n > 0:
        ans += str(n % 2)
        n = int(n / 2)
for i in ans:
    if i == '1':
        sum += 1
print(sum)
