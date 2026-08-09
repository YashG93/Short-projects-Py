
while True:
    choice=int(input('Enter your  choice:\n'
    '1)Kilometer to Miles.\n' 
    '2)Miles to Kilometer.\n' 
    '3)Exit. \n'
    ':  '))
    match choice:
        case 1:
            kilometers=int(input('Enter The KM distance: '))
            conversion_factor=0.621371
            miles=(kilometers*conversion_factor)
            print(f'{kilometers} KM in Miles is {miles} \n')

        case 2:
            Miles=int(input('Enter miles distance: '))
            conversion_factor=0.621371
            kilometers=(Miles/conversion_factor)
            print(f'{Miles} Miles in Kilometer is {kilometers} \n')

        case 3:
            print('GoodBye .')
            break

        case _:
            print('Invalid Choice')