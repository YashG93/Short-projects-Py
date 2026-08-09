
def bmi_cal(weight,height):
    return weight/(height**2)

weight=int(input('Enter body Weight (kg): '))
Height=float(input('Enter Height (m): '))

if weight>0 and Height>0:
    print(bmi_cal(weight,Height))

    if bmi_cal(weight,Height)<18:
        print('Underweight.')

    elif bmi_cal(weight,Height)<25:
        print('Healthy.')
    
    elif bmi_cal(weight,Height)<30:
        print('Overweight.')

    else:
        print('Obese')

else:
    print('Enter valid details.')

