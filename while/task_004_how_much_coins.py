coins = int(input())
cnt = 0

while coins >= 25:
    cnt += 1
    coins -= 25

while coins >= 10:
    cnt += 1
    coins -= 10

while coins >= 5:
    cnt += 1
    coins -= 5

cnt += coins
print(cnt)
