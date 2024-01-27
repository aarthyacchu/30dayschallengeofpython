#'Day 2: 30 Days of python programming'
first_name='Arthy'
last_name='Acchu'
full_name="Aarthy Acchu"
country='India'
city='Banglore'
age=20
year=2003
is_married=False
is_true='name?'
is_light_on=True

#multiple variable
name,country,city,age='Arthy','India','Banglore',20

#finding data types using built in function type()
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#Using the len() built-in function
print(len(first_name))
#print(len(first_name & last_name))

#declaration of one and two
#i
num_one=5     
num_two=4
total=num_one+num_two
print('total',total)

#ii
num_one=5     
num_two=4
diff=num_one-num_two
print('diff',diff)

#iii
num_one=5     
num_two=4
product=num_one*num_two
print('pdt',product)

#iv
num_one=5     
num_two=4
division=num_one/num_two
print('division',division)

#v
num_one=5     
num_two=4
remainder=num_one%num_two
print('rem',remainder)

#vi
num_one=5     
num_two=4
exp=num_one**num_two
print('exp',exp)

#vii
num_one=5     
num_two=4
floor_division=num_one//num_two
print("floordivision",floor_division) 

#area of a circle
radius=30
area_of_circle=2*22/7*radius
print('area of circle',area_of_circle)

#circum of circle
radius=30
circum_of_circle=22/7*radius*radius
print('circm of circle',circum_of_circle)

#radius as user input and calculate the area.
Radius=float(input('enter radius'))
Area_of_circle=2*22/7*Radius
print('the area of circle is:',Area_of_circle)

#use of the built-in input function
First_name=input(str('Enter your first name'))
Last_name=input(str('Enter your last name'))
Country=input(str('Enter your country name'))
Age=int(input('Enter your age'))
print(First_name)
print(Last_name)
print(Country)
print(Age)
