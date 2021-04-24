x,y,z = input().split(' ')
x = int(x)
y = int(y)
z = int(z)

current = 0
count = 0
while(1):
    count += 1
    current += x
    if current >= z:
        break
    current -= y

print(count)