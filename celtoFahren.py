while True:
    try:
        choice=int(input('Enter your choice. \n 1)Celsius To Fahrenheit. \n 2) Fahrenheit To Celsius. \n 3)Exit. \n : '))

        match choice:
            case 1:
                Celsius=int(input('Enter celsius value: '))
                print(f'{Celsius} celsius is {(Celsius * 9/5 )+32} Farhrenite \n')
            
            case 2:
                Farhrenite=int(input('Enter celsius value: '))
                print(f'{Farhrenite} farhrenite is {(Farhrenite -32)*5/9} Celsius \n')

            case 3: 
                break

            case _:
                print('Invalid choice .')

    except  ValueError as e:
        print('Enter correct value. ',e)

