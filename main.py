#Notes Basics

# Escape sequences
# print("this is \\\\ backslash")
# print("these are mountains /\/\/\ ok")
# print("he is \t awesome")
# print("\\ \"\\n \\t \\'")
# print("rohit\n\\")
# print("rohit \\n tejal")
# print("Hello World from github Desktop")

#print type
# print("\U0001F602")
# print("😂")
# name='roit'
# age='23'
# print(f"hello my name is {name} and age is {age}")
# print("hello my name is {} and age is {}".format(name,age))
# print("hello my name is "+name+" and age is "+ age)


#string methods
name='rohitR'
# reverse=name[-1::-1]  reverse
# reverse=name[::-1]    reverse
# print(reverse)
# print(name[:])
# print(name[:-1])
# print(name.count('r'))
# name.upper()     name.lower()      name.title()      name.lstrip()    name.rstrip()     name.strip()
# name.replcae("r","c")   name.find("r",from_index_position_from_where_we_have_to_start_searching)
# print(name.center(9,"*"))  output **rohit**
# print(name.index('r'))

#step argument
# for i in range (0,12,2):
#     print(i)

# list methods
#
# lst.append()
# lst=list(range(1,11))
# lst.insert(position,elemnt)
# lst1=[1,2]
# lst2=[3,4]
# lst3=lst1+lst2          makes new list with addition of two list
# lst1.extend(lst2)       extends lst1 with lst2
# lst.pop()               delete last element of list
# lst.pop(position)       deletes element at postion
# del lst[position]       deletes element at postion
# lst.remove(element)     removes the element irrespective of its position
# lst.count(element)      gives count of element
# lst.sort()              sorts given original list
# sorted(lst)             gives sorted list but does not sort original list lst
# lst.clear()             delete all elements in list
# lst_copy=lst.copy()     copies list
# lst.reverse()           reverses original list
# lst.index(element)      returns element
# lst.index(element,start,stop)       we can specify where to start and where to stop
# popped_item=lst.pop()               delets element and returns deleted item as well

# lst1=[1,2]
# lst2=[1,2]
# print(lst1==lst2)       True
# print(lst1 is lst2)     False

# lst=['rohit','sandanshiv@capgemini','com']
# str='.'.join(lst)
# print(str)              rohit.sandanshiv@capgemini.com

# lst=list(range(1,11))
# print(lst)                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# min(lst)                  returns min of lst
# max(lst)                  returns max of lst

# kk=lambda x:x*x
# print(kk(4))             Lambda function
# le=lambda str:True if len(str)>4 else False       if else lambda

# y=map(func,value)        map function

#tupels
# tuple=(1,2,3) we cannot append insert pop and remove from tuple they are immutable like strings
#tupels are faster than lists
# count,index len slicing is allowed
#sum() max() min()

# num=(1)
# num2=(1,)
# print(type(num))       Integer
# print(type(num2))      tuple

# tuples withour parathesis
# names="rohit","omksr","ashwin"
# # print(type(names))           o/p : tuple

#unpacking tuples
# name1,name2,name3=(names)
# print(name1,name2,name3)       3 diff var for tuple unpacking

#if a list is there in tuple we can edit list

# if function returns 2 values then values are returned in tuple
# def hi(x):
#     return 1,2
# print(hi(2))

# tu=tuple(range(1,11))
# print(tu)



# dictionary
# dict={"name":'rohit',"age":25}

# for i in dict (or dict.keys()):
#     print(i)                                  gives keys of dict
# for i in dict.values():
#     print(i)                                  gives values of dict in form of dict-values
# for i in dict.items():
#     print(i)                                  gives key pair in form of tuple

# ele=dict.items()
# print(ele)                                    gives list of  tuple objects

# dict.pop(element)   deletes the element form dict and returns deleted value and requires at least one element in parathesis
# dict.popitem()        deletes random element from dict and return popped item

# dict1={}
# dict2={}
# dict1.update(dict2)    update dict2 key values in dict1

#fromkeys
# dict=dict.fromkeys(['name','age','height'],'Unknown')
# print(dict)                                            {'name': 'Unknown', 'age': 'Unknown', 'height': 'Unknown'}
# dict=dict.fromkeys('abc','Unknown')
# print(dict)                                              {'a': 'Unknown', 'b': 'Unknown', 'c': 'Unknown'}
# dict=dict.fromkeys((range(1,11)),'unknown')
# print(dict)
# dict=dict.fromkeys(['name','age'],['unk','unk'])
# print(dict)                                              {'name': ['unk', 'unk'], 'age': ['unk', 'unk']}

# dict.get(key)                                      returns value of key or if not there then returns null
# dict.get(key,'not found!')                         if key not found prints not found
# dict.clear()                                        clears the dict
# d1=dict.copy()                                      copies the dict
# if we do d1=dict then what channges we do in d1 will change in dict but not in case of copy
# if(d1 is dict)   false in case if copy
# if (d1 is dict)  True in case of d1=dict

# if there are two or more keys with same name then latest value is considered and it overides prvious one

# sets
# can store int string float or all together but you cannot store list or dict in sets
# unorderd collection of unique items
# no repeat
# s={1,2,2}
# print(s)               No repeated {1, 2}
# s[1]                   we cannot perform like this cause it is unordered
# s.add(element)         adds element
# s.remove(element)      removes element if element is not there then gives key error
# s.discard(element)       removes element if element is not there then no error is there code will run and remove nothing
# s.clear()
# s.copy()
# union_set=s1|s2
# intersection_set=s1&s2
# (s1.issubset(s2)    checks whether s1 is subset of s2)
#(s1^s2) returns s1+s2-intersection


# Advanced Notes:

# List comprehension
# lst=[i*i for i in range (2,11)]                                            prints square of num
# lst=[i for i in range(2,11) if i%2==0] or lst=[i for i in range (2,11,2)]  prints even num
# lst=[i if (i%2==0) else -i for i in range(0,11)]
# lst2=[[i for i in range (1,4)] for i in range (0,3)]               o/p : [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# Dict comprehension
# dict={i:i*i for i in range(0,4)}                       {0: 0, 1: 1, 2: 4, 3: 9}
# dict={f'square of {i} is':i*i for i in range(0,4)}     {'square of 0 is': 0, 'square of 1 is': 1, 'square of 2 is': 4, 'square of 3 is': 9}
# dict={i:'rohitr'.count(i) for i in 'rohitr'}           {'r': 2, 'o': 1, 'h': 1, 'i': 1, 't': 1}
# dict={i:('even' if i%2==0 else 'odd') for i in range (1,11)}  odd even


#sets comprehension
#similar to list



# * operator args
# def total(*args):
#     print(sum(args))
# print(total(1,2,3,4,5,7))         send how many arguments you want it will be converted into tuple and will give us result
# we can keep any name instead of args but generally keep args

# def total(num,*args):
#     print(num)
#     print(sum(args))
# total(1,2,3,4)          num=1 args=2,3,4 so sum will be 2+3+4

# def total(*args,num):      not allowed becuase all parameters will be considered as args and none will specify to num


# lst=[1,2,3,4]/(1,2,3,4)
# def total(*args):
#     return sum(args)       *lst will unpack values and send it to tuple if we simply pass lst
# print(total(*lst))         then sum function will not operate

# def pow(num,*args):
#     if args:
#         return [i**num for i in args]
#     else:
#         return "heey baka"
# lst=[1,2,3]
# print(pow(2,*lst))


# kwargs (keyword arguments)
# **kwargs (double star operator)

# It will return dict {'fname': 'rohit', 'lname': 'sandanshiv', 'domain': '@gmail.com'}
# def heyyo(**kwargs):
#     print(kwargs)
# heyyo(fname='rohit.',lname='sandanshiv',domain='@gmail.com')


# def heyyo(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():                                             kwargs act like dictionary
#         print(k,":",v)
# dict={'fname': 'rohit', 'lname': 'sandanshiv', 'domain': '@gmail.com'}
# heyyo(**dict)                 unpacking dict using **dict_name

# def mixed(name,*args,**kwargs):
#     print(name,args,kwargs)
# mixed('rohit',1,2,3,age=24,sl=2)                o/p: rohit (1, 2, 3) {'age': 24, 'sl': 2}
# order shoudld be PADK
# parameteres,args,default parameters,kwargs


# le=lambda str:True if len(str)>4 else    lambda if else


# Enumerate function
# lst=['rohit','omkar','ashwin']
# pos=0
# for i in lst:
#     print(f"{pos}--->{i}")
#     pos+=1

# for pos,i in enumerate(lst):             enumerate is replacment of above code where position and
#     print(f"{i}--->{lst[i]}")            element simultaneously iterates








# def dec_to_bi(x):
#     if x==0:
#         return 0
#     binary=''
#     while x>0:
#         reminder=x%2
#         binary=str(reminder) + binary
#         x//=2
#     return binary
# print(dec_to_bi(5))

#
# x=sorted('myY naMe is Rohit rohit And and'.split(),key=str.lower)
# print(x)

# def dec_bin(num):
#     if num == 0:
#         return 0
#     st = ''
#     while num > 0:
#         rem = num % 2
#         st += str(rem)
#         num //= 2
#     return st
# print(dec_bin(5))

# def dec_bin(num):
#     if num == 0:
#         return 0
#     st = ''
#     while num > 0:
#         rem = num % 2
#         st += str(rem)
#         num //= 2
#     return st


def myfunc():
    l1 = "my name is rohit"
