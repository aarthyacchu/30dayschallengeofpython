#'Day 10: 30 Days of python programming'
#Q1
#using for loop
'''for i in range(0,11):
    print('using for loop',i)

#using while loop
i=0
while i<10:
    i+=1
    print('using while loop',i)

#Q2
for i in range(1,10):
    print(i-1)


#using while loop
i=10
while i>0:
    print(i)
    i-=1
    
#Q3
for i in range(7):
    print(i+1,(i+1)*"#")
    
#Q4
for name in range(8):#row
    for j in range(8):#col
        print("#",end="")
    print()

#Q5
num=5
i=0
for i in range(1,11):
    #print(i*1,i+1)
    print(f"{5}x",i,"=",i*num)

#Q6
skill=['Python', 'Numpy','Pandas','Django', 'Flask'] 
for skills in skill:
    print(skill)

#Q7
count=0
for i in range(1,100):
    if i%2==0:
        
        print(i)
        count+=1 
print(f"you have {count} even numbers")

#Q8
count=0
for i in range(1,100):
    if i%2!=0: 
        print(i)
        count+=1 
print(f"you have {count} even numbers")'''

#LEVEL 2
#Q1
sum=0
numbers=1
for i in numbers:
    sum=sum+numbers
print(sum)