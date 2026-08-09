from addExpense import __addExpense ,__subExpense,__totalExpense
print('Welcome to Daily expense tracker')
while True:
    try:
        choice=int(input('Enter \n 1.Add expense \n 2.Subtract expense \n 3.Total expense :\n'))
   
        if choice==1:
            num=float(input('Add Expense: '))
            __addExpense(num)
            
        elif choice==2:
            num=float(input('Delete expense: '))
            __subExpense(num)

        elif choice == 3:
            total = __totalExpense()
            print("Total Balance:", total)

        else:
            print('Choose correct option')

    except ValueError:
        print('Enter correct number')