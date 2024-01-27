#'Day 11: 30 Days of python programming'
#Q1
'''def add_two_numbers(a,b):
    sum=a+b
    print(sum)
add_two_numbers(2,2)

#Q2
def area_of_circle(r):
    pi=3.14
    area = pi*r*r
    print(area)
area_of_circle(7)

#Q3
def all_numbers(*nums):
    total=0
    num=[]
    for num in nums:
        total+=num
    return total
print(all_numbers(2,2,2))
num=[2]
if type(num)==int:
        print("valid")

def add_all_nums(*args):
    # Check if all the list items are numbers
    if all(isinstance(item, (int, float)) for item in args):
        # Sum all the arguments
        return sum(args)
    else:
        return "Please provide only numbers as arguments." '''

def all_numbers(*args):
    if all(isinstance(item,(int))):
        for item in args:
            total+=total
        print(total)
        print(all_numbers(1,2,3))
    else:
        return "print valid"

