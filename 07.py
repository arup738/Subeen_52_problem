t = int(input())
i = 0
for i in range(t):
    num = input()
    l = len(num)
    j = 0
    c = 0
    sp = 0
    result=[]
    temp=""
    for j in range(l):
        if num[j] >= "0" and num[j] <= "9":
            temp=temp+num[j]
        else:
            if len(temp)>0:
                result.append(int(temp))
            temp=""
    if len(temp) > 0:
        result.append(int(temp))
    #for index, value in enumerate(result):
     #   print(index, value)
    print(len(result))
