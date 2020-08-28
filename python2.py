Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Araays and lists
>>> a='hello python'
>>> a[0]
'h'
>>> a[1:2]
'e'
>>> a[2:6]
'llo '
>>> a[-1]
'n'
>>> a[-3]
'h'
>>> a[-4]
't'
>>> a[0:6]
'hello '
>>> #slicing-range(start,end)
>>> a[2:4,5:9]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[2:4,5:9]
TypeError: string indices must be integers
>>> len(a)
12
>>> a
'hello python'
>>> #function of strings- find,split,format
>>> #pattern-str.func_name(argument)
>>> "hello python".find("python")
6
>>> #find func helps us to find the argument exists in the string or no
>>> #with the index number
>>> "hello".find("suhr")
-1
>>> #shows the string is not present in the string
>>> "python hello python".find("python",2)
13
>>> "python python python helo".find("python",5)
7
>>> a="nisha hiremani"
>>> b=[32,21,23,56,67]
>>> b[-1]
67
>>> c=["nisha","hiremani"]
>>> a
'nisha hiremani'
>>> "nisha hiremani".split()
['nisha', 'hiremani']
>>> #if you do not write the arg then it will split the string from space
>>> a.split()
['nisha', 'hiremani']
>>> a.split(a)
['', '']
>>> a.split("a")
['nish', ' hirem', 'ni']
>>> #a will be removed from the list
>>> q=a.split("a")
>>> q[1]
' hirem'
>>> c=a.split
>>> a
'nisha hiremani'
>>> c
<built-in method split of str object at 0x03081278>
>>> c=a.split()
>>> a
'nisha hiremani'
>>> c
['nisha', 'hiremani']
>>> c[0][1]
'i'
>>> c[0][0]
'n'
>>> q=c[0]
>>> q[0]
'n'
>>> q
'nisha'
>>> ## format
>>> a="today is good day:"
>>> a="today is good day: {} and tommorow will be {} and after month {}"
>>> t=22
>>> t=221
>>> to=43
>>> one=19
>>> A=a.split("{}")
>>> A
['today is good day: ', ' and tommorow will be ', ' and after month ', '']
>>>  A1=A[0]+str(t)+A[1]+str(to)+A[2]+str(one)
 
SyntaxError: unexpected indent
>>> A1=A[0]+str(t)+A[1]+str(to)+A[2]+str(one)
>>> A1
'today is good day: 221 and tommorow will be 43 and after month 19'
>>> #this is take so much time and efforts
>>> a.format(t,to,one)
'today is good day: 221 and tommorow will be 43 and after month 19'
>>> # {} are replaced with the values
>>> a.format(6,5,5)
'today is good day: 6 and tommorow will be 5 and after month 5'
>>> a.format("happy","sad or happy","sad")
'today is good day: happy and tommorow will be sad or happy and after month sad'
>>> 
>>> ##playing with lists and arrays
>>> x=[1,2,3,4,5,5,6,7]
>>> y=[2,4,5,6,7,8,9]
>>> z=[1,3,4,5,"hello",5.6,90]
>>> type(x)
<class 'list'>
>>> type(y)
<class 'list'>
>>> type(z)
<class 'list'>
>>> ## array can save only one type of data and list can save all types of data like - strings ,int float
>>> ##func of list-append,index,pop
>>> #pattern-list.func(arg) -optional
>>> ##append-add value in last position
>>> x.append(100)
>>> x
[1, 2, 3, 4, 5, 5, 6, 7, 100]
>>> a.index(1,67)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.index(1,67)
TypeError: must be str, not int
>>> a.insert(1,67)  ##a.insert(loc,value)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    a.insert(1,67)  ##a.insert(loc,value)
AttributeError: 'str' object has no attribute 'insert'
>>> a.insert(1,67)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.insert(1,67)
AttributeError: 'str' object has no attribute 'insert'
>>> a.insert(1, 67)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.insert(1, 67)
AttributeError: 'str' object has no attribute 'insert'
>>> x.insert(2,67)
>>> x
[1, 2, 67, 3, 4, 5, 5, 6, 7, 100]
>>> x.index(2)
1
>>> ##searching index of the value index is used
>>> ##pop
>>> x.pop()
100
>>> x.pop(2)
67
>>> x
[1, 2, 3, 4, 5, 5, 6, 7]
>>> x.pop('4')
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    x.pop('4')
TypeError: 'str' object cannot be interpreted as an integer
>>> x.pop(,4)
SyntaxError: invalid syntax
>>> x.index(6)
6
>>> x.pop(6)
6
>>> x
[1, 2, 3, 4, 5, 5, 7]
>>> x.index(5)
4
>>> x.pop(4)
5
>>> x
[1, 2, 3, 4, 5, 7]
>>> x.append(5)
>>> x
[1, 2, 3, 4, 5, 7, 5]
>>> x.removed(5)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    x.removed(5)
AttributeError: 'list' object has no attribute 'removed'
>>> x.remove(5)
>>> x
[1, 2, 3, 4, 7, 5]
>>> 
>>> ##dict