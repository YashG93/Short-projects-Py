from expense import conn,cursor

def __addExpense(num):
    cursor.execute("insert into expenses (amount,type) values (%s,%s)",(num,'add'))
    conn.commit()
    print(f'{num} added successfully')

def __subExpense(num):
    cursor.execute('insert into expenses (amount,type) values(%s,%s)',(num,'sub'))
    conn.commit()
    print(f'{num} subtracted successfully')

def __totalExpense():
    cursor.execute('SELECT amount, type FROM expenses')
    rows = cursor.fetchall()

    total = 0

    for amount, t in rows:
        if t == 'add':
            total += amount
        else:
            total -= amount

    return total

