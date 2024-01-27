#'Day 4: 30 Days of python programming'
#Q1
string1=['Thirty', 'Days', 'Of', 'Python']
result='_'.join(string1)
print(result)

#Q2
string2=['Coding', 'For' , 'All' ]
result='_'.join(string2)
print(result)

#Q3
company="Coding For All"
#Q4
print(company)
#Q5
print(len(company))
#Q6
print(company.upper())
#Q7
print(company.lower())
#Q8
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Q9
cut=company[1:-1]
print(company)

#Q10
print(company.index('Coding'))
print(company.find('Coding'))

#Q11
print(company.replace('Coding','python'))

#Q12
print(company.replace('python for all','python for everyone'))

#Q13
company='Coding For All'
print(company.split())

#Q14
company="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(','))

'''#Q15
company='Coding For All'
print(company.index(0))

#Q16
print(company.rindex(-1))

#Q17
print(company.index(10))

#Q18, 19'''

#Q20
company='Coding For All'
substring1='C'
print(company.index(substring1))

#Q21
company='Coding For All'
substring2='F'
print(company.index(substring2))

#Q22
company='Coding For All'
substring3='l'
print(company.index(substring3))

#Q23
sentence="You cannot end a sentence with because because because is a conjunction"
substring4='because'
print(sentence.index(substring4))

#Q24
sentence="You cannot end a sentence with because because because is a conjunction"
substring5='because'
print(sentence.rindex(substring5))

#Q25
chop=sentence[31:18]

#Q26
print(sentence.find('because'))

#Q27
Chop=sentence[0:30:17]

#Q28
company='Coding For All'
print(company.startswith('Coding'))

#Q29
company='Coding For All'
print(company.endswith('coding'))

#Q30

#Q31
var1='30DaysOfPython'
print(var1.isidentifier())
var2='thirty_days_of_python'
print(var2.isidentifier())

#Q32
libraries=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result='#'.join(libraries)
print(result)

#Q33
print("I am enjoying this challenge\n I just wonder what is next.")

#Q34
print('name\tage\tcountry\tcity')
print('Asabeneh\t250\tFinland\tHelsinki')

#Q35
radius = 10
area = 3.14 * radius ** 2
formated_str='The area of a circle with radius {} is {} meters square'.format(radius,area)
print(formated_str)

#Q36
a=8
b=6
print(f'{a} + {b}={a+b}')
print(f'{a} - {b}={a-b}')
print(f'{a} * {b}={a*b}')
print(f'{a} / {b}={a/b}')
print(f'{a} % {b}={a%b}')
print(f'{a} // {b}={a//b}')
print(f'{a} ** {b}={a**b}')