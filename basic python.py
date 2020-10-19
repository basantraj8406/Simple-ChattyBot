# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 14:40:37 2020

@author: BASANT RAJ
"""

city="Bihar"
cityStrip="*****  Bihar  *****"
caption='land of IAS'
subject='Learning Python in 3rd semester .'
punc=','
seq=(city,caption)#tuple
print(type(city))#caption,subject)

print(len(city)) #length of the string

print(city.swapcase())

print(caption.title())
print(cityStrip.strip())
print(cityStrip.strip('*')) #Removing Character
print(cityStrip.lstrip('*')) #Left strip
print(cityStrip.rstrip('*')) #right Strip
print(city.count('a')) #number of occurence
print(city.count('a',3,len(city))) #number of occurence with limit
print(city.find('a'))#finds first occurence from left or begning
print(city.find('o'))
print(city.rfind('a')) #finds first occurnce from right or last
print(punc.join(seq)) #we need touple to do this type of wor otherwise it will not work
#print(punc.join(city,caption))  -> it will not work
print(subject.split())