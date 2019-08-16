a,b,c = map(int, input().split())
answer = []
answer.append(a+b*c)
answer.append(a*(b+c))
answer.append(a*b*c)
answer.append((a+b)*c)
print(max(answer))