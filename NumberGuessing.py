import random
num=random.randint(1,2)
print(num)
while True:
    guess=int(input("guess the number between (1-10): "))

    if guess==num:
        print('correct')
        break
    else:
        print('Try again')
