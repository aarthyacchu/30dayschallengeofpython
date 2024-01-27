#'Day 5: 30 Days of python programming'
#Q1
list=[]
#Q2
list=['one','two','three','four','five','six']
#Q3
print(len(list))
#Q4
first_item=list[0]
print('first item',first_item)
middle_item=list[2]
print('middle item',middle_item)
last_item=list[-1]
print('last item',last_item)
#Q5
mixed_data_types=['Arthi',20,5.3,False,{'countru':'India','city':'Karnataka'}]
#Q6
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#Q7
print("it company list:",it_companies)
#Q8
print('lenth of IT companies:',len(it_companies))
#Q9
first_company=list[0]
print('first company',first_company)
middle_company=list[2]
print('middle company',middle_company)
last_company=list[-1]
print('last company',last_company)
#Q10
it_companies[0]='instagram'
print('modified company list:',it_companies)
#Q11
it_companies.append('Facebook')
print('after adding an item to list:',it_companies)
#Q12
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.insert(2,'SQL')
print('after adding company in middle',it_companies)
#Q13
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies[-1]='AMAZON'
print('After changing last item to caps',it_companies)
#Q14

#Q15
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
does_exist='BMI' in it_companies
print('checking if IBM is in the list:',it_companies)
#Q16
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort()
print('sorted it companies',it_companies)
#Q17
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.sort(reverse=True)
print('sorted list in decending order',it_companies)
#Q18
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
rest=it_companies[:-3]
print('list after slicing 1st three',rest)
#Q19
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
begning=it_companies[-3:]
print('after sclicing beginig of list:',begning)
#Q20
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
mid=it_companies[0:-2:3]
print('after slicing mid items',mid)

#Q21
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.pop(0)
print('after poping 1st item',it_companies)
#Q22
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.pop(2)
print('after poping mid item',it_companies)
#Q23
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.pop()
print('after poping last item',it_companies)
#Q24
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.clear()
print('empty list',it_companies)
#Q25
it_companies =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
del it_companies
print('after deleting the list',it_companies)

#Q26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
list_3=front_end+back_end
print('after joining the list',list_3)
#Q27
full_stack=list_3.copy()
print('copied list',full_stack)

