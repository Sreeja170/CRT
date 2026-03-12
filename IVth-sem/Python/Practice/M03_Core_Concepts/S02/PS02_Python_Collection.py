'''
#2)accessing of list; index0, -1
a = [1,23,45,68]
print(a)
print(a[1])
print(a[-2])
print(a[-1])


#3)creating list with repeated elements
a= [1,2,3]
print(a*2)


#4)adding elements to a list





#5)removing elements from list
b = list((1,23,4,5,7,98))
print(b)
b.remove(7)
print(b)
b.pop




3)sets: {}

#creation of set:
a = {1,2,3,4,5,6}
print(a)
b = set([1,2,3,45,5])
print(b)

#adding elements in set:
b = set([1,2,3,45,5])
print(b.add(50))


#removing
b = set([1,2,3,45,5])
print(b)


#set operations:
a = {1,2,3,5,6}
b = {10,2,3,5,60}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


t = (1,23,45,50)
print(t)


#accessing of tuples:

#concatenation
t1 = (1,23,45,50)
t2 = (1,2,87,9,6)
print(t1 + t2)

#nesting of tuples
t1 = (1,23,45,50)
t2 = (1,2,87,9,6)
print(t1 , t2) 


#repetition of tuples
t1 = (1,23,45,50)
print(t1[1:])
print(t1[0:3])
print(t1[:-1])


#deleting a tuple:
t1 = (1,23,45,50)
del t1


'''
#creating ({}, dict())
d = {'name':'sreeja', 'age':19}
print(d)
d = dict(name='sreeja', age =19)
print(d)

#accessing dict items(key[], get()):
d = {'name':'sreeja', 'age':19}
d.key['name']
print(d)
d.get('name')
print(d)

#adding and updating dict items (assignment)
d = {'name':'sreeja', 'age':19}
d['phn'] = 9381903609
print(d)


#removing dict items (del, pop()-->remove key but return value, clear()-->empty dict)
d = {'name':'sreeja', 'age':19}
del d['age']
d.pop('name')
print(d)
d.clear()
print(d)

