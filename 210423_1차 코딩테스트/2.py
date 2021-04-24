length, won = input().split()

length = int(length)
won = int(won)

arr = list(range(length))

for i in range(length):
    
    arr[i] = input()
    arr[i] = int(arr[i])

arr.reverse()
count = 0
total = 0
for i in range(len(arr)):
    if (won/arr[i]) >= 1:
        count = won//arr[i]
        total += count 
        won -= arr[i]*count

print(total)