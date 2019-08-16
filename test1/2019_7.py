n = int(input())
t_sum = 0
for i in range(5,0,-1):
    t_sum += int(n/i)
    n %= i
print(t_sum)
