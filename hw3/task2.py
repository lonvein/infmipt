a = int(input())


def f(n):
    for i in range(2, n+1):
        if n % i == 0:
            return str(i) + ' ' + f(n//i)
    return ' '


print(f(a))
