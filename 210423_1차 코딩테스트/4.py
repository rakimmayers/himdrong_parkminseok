a = list(map(int,input().split()))
b = list(map(int,input().split()))

sum = 0
for i in range(len(a)):
    sum += a[i]*b[i]

print(sum)