pos_alex = -1
pos_lev = -1
current_position = 0

while True:
    name = input()
    if name == "Александра" and pos_alex == -1:
        pos_alex = current_position
    if name == "Левон" and pos_lev == -1:
        pos_lev = current_position
    if pos_alex != -1 and pos_lev != -1 :
        break
    current_position += 1

print(abs(pos_alex - pos_lev) - 1)
