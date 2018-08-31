from datetime import date



def age ():
    yob = int( input('Enter your year :'))
    today_date = date.today().year
    age= today_date - yob
    if age < 18:
        print('Minor')
    elif age >= 18 and age <= 36:
        print('Youth')
    else:
        print('Elder')

age()