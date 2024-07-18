s = input()
parts = s.split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

next_number = c + (c - b)

print(next_number)