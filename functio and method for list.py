# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 11:24:24 2020

@author: BASANT RAJ
"""

lst1=['NSEC',3,2020,"IT","makaut ","IT","it"]
print(lst1)
print(lst1[2])
print(lst1[-1])   #-1 for last item in the list
print(lst1[-1]*3) # astric is repetition operator
print(lst1[1:3]) #colon is slice operator
lst2=[x for x in range(0,10)]
print(lst2)

lst3=[x for x in range(0,10,2)]
print(lst3)

#FUNCTION FOR LIST
print(len(lst2))
print(max(lst2))
print(min(lst2))

#METHOD FOR LIST
lst1.append(100) #insert element at the end of the list
print(lst1)

print(lst1.count("IT")) #no. of items present in a list

del lst1[2]  #first method to remove item
print(lst1)

lst1.remove('NSEC') #if we remove IT then first IT will be removed i.e lowest index will be removed
print(lst1)



print(lst1.index(100))

lst2.extend(lst3)
print(lst2)

lst2.reverse()
print(lst2)

lst1.insert(2,'India')
print(lst1)

lst3.clear() # To remove all the items from the list
print(lst3)

lst4=lst2
print(lst4)

lst3=lst1.copy()
print(lst3)

tup1=tuple(x for x in 'Technology')
print(tup1)

tup2=('nsec',3,2020,'it','makaut')
print(tup2)
print(tup2[3])

del tup2[3]
print(tup2) #tuple doesn't support iten deletion

#FUNCTIONS FOR TUPLE
print(len(tup2))   #doesn't support
print(max(tup2)) #doesn't support
print(min(tup2))  #doesn't support

st1=set(x for x in 'Technology')
print(st1)

st2={'nsec',3,2020,'it'}
print(st2)

st3={0, 1, 2, 3, 4, 5, 6, 7, 8,5,0, 9,3,4}
print(st3)
st4={1,2,3,5,4,5}

st5={}
print(st5)

#FUNCTIONS FOR SET
print(len(st3))
print(max(st3))
print(min(st3))
print(sum(st3))
print(sorted(st4))

print(any(st5)) # check whether a set is empty or not
print(all(st4)) # if there is any 0 in the set then it will print false

#METHOD FOR SETS

st2.add('india')
print(st2)
st2.remove(3)
print(st2)