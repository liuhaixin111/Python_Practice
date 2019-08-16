n = int(input())
a = 1
b = 2
temp_list = [1]
while True:
    if a != n:
        for i in range(b):
            temp_list.append(b)
            a += 1
            if a == n:
                break
        b += 1
    else:
        print(temp_list[-1])
        break