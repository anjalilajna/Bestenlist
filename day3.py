Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={'name':'anjali','id':1234}
>>> dict2={'name1':'riya','id1':6789}
>>> dict1.update(dict2)
>>> print(dict1)
{'name': 'anjali', 'id': 1234, 'name1': 'riya', 'id1': 6789}
>>> lang={'one':'tamil','two':'hindi','three':'english','four':'telugu'}
>>> lang.pop('two')
'hindi'
>>> print(lang)
{'one': 'tamil', 'three': 'english', 'four': 'telugu'}
>>> list1=['name','id']
>>> list2=['lalli',5677]
>>> list_dict=dict(zip(list1,list2))
>>> print(list_dict)
{'name': 'lalli', 'id': 5677}
>>> fruits={"apple","bannana","orange"}
>>> print(len(fruits))
3
>>> s1={1,2,3,4,5,9}
>>> s2={6,7,8,0,1,2}
>>> print(s1-s2)
{9, 3, 4, 5}
>>> 