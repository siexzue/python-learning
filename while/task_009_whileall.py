n = int(input())

total = 0
counter = 0
howmch = 1
product = 0
first = 0
lst_dgt = n % 10

while n > 0:
    last_digit = n % 10
    total += last_digit
    first = last_digit
    counter += 1
    howmch *= last_digit
    product = total / counter


    n //= 10

print(total)
print(counter)
print(howmch)
print(product)
print(first)
print(first + lst_dgt)
