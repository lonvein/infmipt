import math
a, b = map(str, input().split(' '))
print(a[1::-1] + a[2:] + '-' + b[1::-1] + b[2:])
