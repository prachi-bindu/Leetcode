def digital_root(n):
    print(n)
    if n < 10:
        return n
    else:
        sum = 0
        digit = n % 10
        sum = sum + digit
        n = sum
        digital_root(sum)


digital_root(10)