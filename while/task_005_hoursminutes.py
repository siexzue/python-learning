h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

start = h1 * 60 + m1
end = h2 * 60 + m2

current = start

while current <= end:
    hours = current // 60
    minutes = current % 60
    print(f"{hours:02d}:{minutes:02d}")
    current += 1
