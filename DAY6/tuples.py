#'Day 6: 30 Days of python programming'
#Q1
tpl=tuple()
print('Empty tuple:',tpl)
#Q2
brother=('Krithi','aravind','gokul','arulan')
sister=('Mithra','Janani','Ramya','Gayu','aganya','diya')
print('Brothers:',brother)
print('sisters',sister)
#Q3
brother=('Krithi','aravind','gokul','arulan')
sister=('Mithra','Janani','Ramya','Gayu','aganya','diya')
siblings=brother+sister
print('list of siblings=',siblings)
#Q4
len(siblings)
#Q5
siblings=list(siblings)
siblings.clear()
siblings=['niveda','senthil']
#siblings[0]='niveda'
#siblings[1]='senthil'
siblings=tuple(siblings)
print("family members",siblings)