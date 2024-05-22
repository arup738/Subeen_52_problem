t = int(input())
i = 0
for i in range(t):
    num = input()
    l = len(num)
    first = int(num[0])
    last = int(num[l-1])
    sum = first + last
    print("Sum =",sum)