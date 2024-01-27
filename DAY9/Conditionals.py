#'Day 9: 30 Days of python programming'
#1Q
age=int(input("Enter your age"))
if age>=18:
    print("You are old enough to learn to drive.")
else:
    print(f'You need {18-age} more years to learn to drive.')

#2Q
my_age=int(input("Enetr person 1 age"))
your_age=int(input("Enter person 2 age:"))
if my_age<your_age:
    print(f"you are {my_age-your_age} years older than me")
    if my_age>your_age:
        print(f"you are {my_age-your_age} years older than me")

#Q3
a=int(input('Enter num one'))
b=int(input('Enter num tow'))
if a>b:
    print(f"{a} is greater than {b}")
elif a<b:
    print(f"{b} is greater than {a}")
elif a==b:
    print(f"{a} is equal to {b}")

#LEVEL 2
#Q1
score=int(input("Enter the student score"))
if score>=90:
    print("A grade")
    if score<=89:
        print("B grade")
    else:
        print("C grade")
elif score<=59:
    print("D grade")
else:
    print("f grade")

#Q2
month=str(input("Enter the month:"))
#Autumn=['September', 'October', 'November']
if month=="September" or month=="October" or month=="November":
    print("Autumn season")
elif month=='December' or month=='January' or month=='February':
    print("Winter season")
elif month=='March' or month=='April' or month=='May':
    print('Spring season')
else:
    print("Summer season")

#Q3
fruits =['banana', 'orange', 'mango', 'lemon']
uinput=str(input("Enter the fruit")) 
print("fruit already exist in list") if fruits==uinput else fruits.append(uinput)
print("list after adding an item",fruits)

#LEVEL 3
#Q1
'''person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:'''

