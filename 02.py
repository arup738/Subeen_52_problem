t = int(input())
for _ in range(t):
    num_str = input()
    length = len(num_str)
    last_num = int(num_str[length-1])
    if last_num%2==0 :
        print("even")
    else:
        print("odd")