amy = [0,0,0]
emily = [0,0,0]

amy[0], amy[1], amy[2] = input().split()
amy[0] = int(amy[0])
amy[1] = int(amy[1])
amy[2] = int(amy[2])

emily[0], emily[1], emily[2] = input().split()
emily[0] = int(emily[0])
emily[1] = int(emily[1])
emily[2] = int(emily[2])

amy_price = 0
emily_price = 0

for i in range(3):
    if amy[i] > emily[i]:
        amy_price += 1
    elif amy[i] < emily[i]:
        emily_price += 1
    elif amy[i] == emily[i]:
        continue

print(f"{amy_price} {emily_price}")