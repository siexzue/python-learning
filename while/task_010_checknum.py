n = int(input())
flag = 0
last_digit = n % 10

while n > 0:
    lst_dgt = n % 10
    n //= 10
    if last_digit != lst_dgt:
        flag = False #лишний флаг
        break
    else:
        flag = True

if flag is True:
    print("YES")
else:
    print("NO")
