
class DivisibleBySeven:
    def __init__(self,n):
        self.n=n

    def generate_div7(self):
        for num in range(self.n+1):
            if num%7==0:
                yield num

num=int(input('Enter your desired range: '))
div_by7=DivisibleBySeven(num).generate_div7()

for num in div_by7:
    print(num)