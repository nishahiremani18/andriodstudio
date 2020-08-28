Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5+5
10
>>> 5-5
0
>>> 5+-6
-1
>>> 5*3
15
>>> 5**3
125
>>> 5***3
SyntaxError: invalid syntax
>>> 7**3
343
>>> pow(2,4)
16
>>> pow(2,-2)
0.25
>>> x=8
>>> id(x)
1773774880
>>> i=2
>>> j=i
>>> id(i)
1773774784
>>> id(j)
1773774784
>>> id(2)
1773774784
>>> x=3
>>> q=8.9
>>> #id to check particular location
>>> type(x)
<class 'int'>
>>> type(q)
<class 'float'>
>>> s="nisha"
>>> type(s)
<class 'str'>
>>> s+q
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    s+q
TypeError: can only concatenate str (not "float") to str
>>> #s=str q=float
>>> typecasting
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    typecasting
NameError: name 'typecasting' is not defined
>>> #typecasting: convert data types
>>> s
'nisha'
>>> q
8.9
>>> str(q)
'8.9'
>>> s+q
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s+q
TypeError: can only concatenate str (not "float") to str
>>> s+str(q)
'nisha8.9'
>>> a=12
>>> b="12"
>>> a+int(b)
24
>>> str(a)+b
'1212'
>>> #generate 4-digit no
>>> #1st no should bethe half of last no eg:2xx4
>>> #1st 2 digits shd be half of last 2 digits eg:1938 1326 2244
>>> #x22x x33x
>>> ans=4998
>>> 
>>> a=1232
>>> a//100
12
>>> (a/100)-12
0.3200000000000003
>>> a%100
32
>>> print(a)
1232
>>> a
1232
>>> b='hello'
>>> b
'hello'
>>> #b gives ans with its data type and print juz gives you the output without any datatype
>>> print(b,a)
hello 1232
>>> # here no need to convert into another datatype
>>># arrays and lists
a[0]=1

