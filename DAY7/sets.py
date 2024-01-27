#'Day 7: 30 Days of python programming'
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Q1
print('lenth of it companies:',len(it_companies))
#Q2
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it_companies.add('Twitter')
print('after adding tweeter',it_companies)
#Q3
it_companies.update(['YouTube','Instagram','WhatsApp'])
print('after adding multiple it companies',it_companies)
#Q4
it_companies.remove('Twitter')
print('after removing twitter',it_companies)

#LEVEL 2
#Q1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
ab=A.union(B)
print('after joining A and B',ab)
#Q2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('finding A intersection of B:',A.intersection(B))
#Q3
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('Is A subset of B:',A.issubset(B))
#Q4
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('Are A and B disjoint sets',B.isdisjoint(A))
#Q5
print('Join A with B and B with A',B.symmetric_difference(A))
#Q7
del A
del B
#print('del of a',A)
#print('del of b',B)
