n = int(input())
last_digit = n % 10
max = last_digit
min = last_digit
n //= 10

while n > 0:
    last_digit = n % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    n //= 10

print("Максимальная цифра равна", max)
print("Минимальная цифра равна", min)
