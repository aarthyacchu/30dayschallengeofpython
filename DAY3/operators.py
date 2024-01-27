#'Day 2: 30 Days of python programming'   (Q1,2,3)
age=20 
height=5.4
#i=1+4

#Q4
base=float(input("Enter the base"))
height=float(input("Enter the height"))
area_of_triangle=0.5*base*height
print("area of triangle=",area_of_triangle)

#Q5
a=int(input("Enter side a"))
b=int(input("Enter side b"))
c=int(input("Enter side c"))
perimeter=a+b+c
print("The primeter of the triangle=",perimeter)

#Q6
length=float(input("Enter the length of rect"))
width=float(input("Enter the width of rect"))
area_of_rect=length*width
perimeter_of_rect=2*length+width
print("area of rectangle=",area_of_rect)
print("primeter of rect=",perimeter_of_rect)

#Q7
radius=float(input('enter radius'))
area_of_circle=2*22/7*radius
circum_of_circle=22/7*radius*radius
print('The area of circle is:',area_of_circle)
print('The circmference of circle',circum_of_circle)

#Q8,9,10,11 Euclidean distance
#Q12
print(len('python') and len('dragon'))
print("python is dragon =",'python' == 'dragon')

#Q13
print("on in python and dragon = ",'on' in 'python and dragon')

#Q14
print("jargon in I hope this course is not full of jargon =",'jargon' in 'I hope this course is not full of jargon')

#Q15
print("no ont in dragon and python",'on' not in 'dragon' and 'python')

#Q16
print(len('python'))   #redo
float(6.0)
print(type(6.0))
string('6.0')
print(type('6.0'))

#Q17
num=int(input("Enter a number"))
if num%2==0:
    print("even number")
else:
    print("odd number")

#Q18
print("If the floor division of 7 by 3 is equal to the int converted value of 2.7.",7//3 == 2.7)

#Q19
#print("if type of '10' is equal to type of 10",'10' == 10)
print('10'==10)

#Q20
print("if int('9.8') is equal to 10", 9.8 == 10)

#Q21
hour=int(input("Enter the hours="))
rate=int(input("Enter the rate per hour"))
weekly_earning=hour*rate
print('weekly earning=',weekly_earning)