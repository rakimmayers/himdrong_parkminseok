num1,num2,num3,num4,num5 = input().split()

nums = [int(num1),int(num2),int(num3),int(num4),int(num5)]

temp = nums

min = 0
max = 0

nums.sort()

for i in range(4):
    min += nums[i]


nums.reverse()

for i in range(4):
    max += nums[i]


print(f"{min} {max}")