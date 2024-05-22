t=int(input())
for i in range(t):
    str=input()
    result=[]
    temp=""
    for j in range(len(str)):
        if "0"<=str[j]<="9":
            temp=temp+str[j]
        else:
            if len(temp)>0:
                result.append(int(temp))
            temp=""
    if len(temp) > 0:
        result.append(int(temp))
    print("Case", i + 1, end=":")
    result.sort()
    for k in range(len(result)):
            print(end=" ")
            print(result[k], end="")
    print()





