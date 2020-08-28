Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##dict
>>> l=[[1,2,3],[2,5,6]]
>>> ##key-value
>>> a={"name":"nisha"}
>>> a["name"]
'nisha'
>>> a={"no":i48379164}
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a={"no":i48379164}
NameError: name 'i48379164' is not defined
>>> a={"no":564738920}
>>> a["no"]
564738920
>>> a={"name":"nisha","age":21,"class":12}
>>> a["class"]
12
>>> a["gender"]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a["gender"]
KeyError: 'gender'
>>> #gender doesnot exists in key
>>> a={"name":"nisha","age":21,"class":12,"name":"amisha"}
>>> a["name"]
'amisha'
>>> #data or value is replaced with new value
>>> a
{'name': 'amisha', 'age': 21, 'class': 12}
>>> a={"key":"value"}
>>> a["key"]
'value'
>>> type(a)
<class 'dict'>
>>> ##1-D dict
>>> ## 2-D
>>> a["key"]="nisha"
>>> a["key"]
'nisha'
>>> a
{'key': 'nisha'}
>>> a["gender"]="female"
>>> a
{'key': 'nisha', 'gender': 'female'}
>>> a["beats"]=123
>>> a
{'key': 'nisha', 'gender': 'female', 'beats': 123}
>>> a["beats"]["sound"]=123
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a["beats"]["sound"]=123
TypeError: 'int' object does not support item assignment
>>> a["beats"]={}
>>> a
{'key': 'nisha', 'gender': 'female', 'beats': {}}
>>> a["beats"]["sound"]="dj"
>>> a
{'key': 'nisha', 'gender': 'female', 'beats': {'sound': 'dj'}}
>>> a["beats"]["no"]=123
>>> a
{'key': 'nisha', 'gender': 'female', 'beats': {'sound': 'dj', 'no': 123}}
>>> a["beats"]["no"]
123
>>> 