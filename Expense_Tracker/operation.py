bal=0

def Add_exp(amount):
    global bal
    bal=bal-amount
    return bal

def Add_amt(amount):
    global bal
    bal=bal+amount
    return bal

def Total_bal():
    return bal