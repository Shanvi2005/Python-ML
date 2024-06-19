num=[1,22,32,11,134,23,76,98]
minimum = num[0]
maximum = num[0]
for i in num:
    minimum = min(minimum, i)
    maximum = max(maximum, i)
print("maximum",maximum)
print("minimum",minimum)
