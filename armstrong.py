n = int(input("Find Armstrong numbers up to: "))

for num in range(1, n + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == num:
        print(num)