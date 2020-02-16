#!/usr/bin/env python
# coding: utf-8
 
# # Python 기초
#
# 여러분들은 이 코스에서 파이썬의 기초 문법을 다루게 됩니다. 본 코스는 크게 4단계로 나누어집니다.
#
# 1. Assignment
# 2. Flow Control
# 3. Data Structures
# 4. Functions
 
# ## 0. 사전 작업
 
# In[ ]:
 
 
# print
print('hello world')
 
 
# In[ ]:
 
 
name = '홍길동'
age = 40
height = 180.1234
 
print('제 이름은 %s이고, 나이는 %d세입니다. 키는 %fcm입니다.' % (name, age, height))
print('제 이름은 %s이고, 나이는 %d세입니다. 키는 %dcm입니다.' % (name, age, height))
print('제 이름은 %6s이고, 나이는 %.2f세입니다. 키는 %0.2fcm입니다.' % (name, age, height))
 
 
# In[ ]:
 
 
# 주석처리
"""
안녕하세요. 저는 고태훈입니다.
파이썬의 세계에 오신 것을 환영합니다.
"""
print('hello world')
 
 
# ### Jupyter notebook
# - 직관적으로 파이썬을 구현해보기에도 좋고, 문서화하여 잘 정리하는 목적으로도 좋습니다.
# - 심지어 HTML 태그까지 삽입해서 웹 페이지를 만드는 데에도 이용할 수 있다고 합니다.
# - 과거에는 ipython notebook으로 불렸는데, Jupyter notebook으로 변화하면서 python 외에 여러 언어를 지원하고 있습니다.
# - 단축키를 활용하면 매우 좋습니다! (셀이 선택되어 있지 않은 상태에서) h를 눌러보세요. 다음과 같은 이미지를 볼 수 있습니다.
 
# In[ ]:
 
 
# image를 출력할 수 있는 라이브러리
from IPython.display import Image
Image(filename="keyboard_shortcuts.png")
 
# 몇 가지 간단한 명령어를 사용해 보자!
 
# cell 생성 및 삭제
# 방금 삭제한 셀 복구
# 마크다운, heading 1~4
 
 
# ## 1. Assignment
#
# 파이썬에서는 매우 편하게 변수를 정의하고 이에 대한 값을 넣을 수 있습니다.
# 프로그래밍을 해보신 분들은 assignment와 각 변수의 type에 대해서 잘 아실겁니다.
 
# ### Strings
#
# 문자열을 할당하는 방법입니다. ''와 "" 모두 사용 가능합니다.
#
# 문자열이 각 문자의 array로 표현됨을 알 수 있습니다. (You can access characters in the string using array syntax.)
 
# In[ ]:
 
 
first = 'hello world'
second = "hello world"
print(first)
print(second)
print(first[0])
print(first[-3])
print(len(first))
print(first[len(first)-3])
print(first[0:3])
 
 
# In[ ]:
 
 
# 문자열에 작은 따옴표 포함시키기
test = "I'm a boy"
print(test)
 
# 문자열에 큰 따옴표 포함시키기
test = '"I love you." he said'
print(test)
 
# 백슬래시 활용
test = '\"I\'m a boy.\" he said'
print(test)
 
 
# In[ ]:
 
 
# \n을 이용하여 여러 줄의 문자열을 변수에 할당
multiline = 'I\'m fine, thank you.\nAnd you?'
print(multiline)
 
# 따옴표 3개를 활용
multiline = '''
I am a boy
You are a girl
'''
print(multiline)
 
multiline = """
I am a boy
You are a girl
"""
print(multiline)
 
 
# In[ ]:
 
 
# escape character code using backslash
tab = 'a\tb'
print(tab)
enter = 'a\nb'
print(enter)
backslash = 'a\\b'
print(backslash)
 
 
# In[ ]:
 
 
# Concatenation
head = 'Python'
tail = ' is fun!'
print(head+tail)
 
 
# ### Numbers
 
# In[ ]:
 
 
Image(filename="numeric_system.png")
 
 
# In[ ]:
 
 
# Numbers
value = 123
print(value)
value = 123.123
print(value)
value = -123.123
print(value)
 
 
# In[ ]:
 
 
# 숫자 연산자
a = 5
b = 2
print(a + b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
 
 
# ### Boolean
# True와 False 값을 갖는 형태입니다. 그리고 ==, !=, >, >= 등을 통해 주어진 명제가 True인지 False인지 판단할 수 있습니다.
 
# In[ ]:
 
 
# Boolean
t = True
f = False
print(t,f)
 
a = 1
b = 2
c = a + b == 4
d = a + b == 3
e = a + b > 3
f = a + b >= 3
g = a + b != 3
print(c)
print(d)
print(e)
print(f)
print(g)
 
 
# ### Multiple Assignment
 
# In[ ]:
 
 
# Multiple Assignment
a, b, c = 1, 2, 3.3
print(a,b,c)
 
 
# ### No Value
# 값이 없는 경우를 None이라는 형태로 할당할 수 있습니다.
 
# In[ ]:
 
 
a = None
print(a)
 
 
# ## 2. Flow Control
# Flow control은 프로그래밍에서 매우 중요한 요소입니다. 여기서는 3가지 방법을 소개합니다.
 
# ### If-then-else conditional
# if, elif, else를 이용하여 다양한 조건문을 생성할 수 있습니다.
# 들여쓰는 것은 tab을 이용하는 방법과 스페이스4번(공백4개)를 이용하는 방법이 있는데, 가급적 후자를 권장합니다.
 
# In[ ]:
 
 
a = 1
b = 5
 
if a + b == 3:
    print("correct")
else:
    print("wrong")
 
 
# In[ ]:
 
 
value = 50
if value == 99:
    print('That is fast')
elif value > 200:
    print('That is too fast')
else:
    print('That is safe')
 
 
# In[ ]:
 
 
value = 99
if value == 99: print('That is fast')
elif value > 200: print('That is too fast')
else: print('That is safe')
 
 
# ### For-loop
# 가장 널리 쓰이는 반복문입니다. 파이썬이 매우 직관적인 언어라는 것을 알 수 있습니다.
 
# In[ ]:
 
 
for i in range(10):
    print(i)
 
 
# In[ ]:
 
 
# range(a,b): a 이상 b 미만의 모든 정수
for j in range(-2,5): print(j)
 
 
# In[ ]:
 
 
for j in range(-2,5):
    print(j)
 
 
# In[ ]:
 
 
test = [(1,2), (3,4), (5,6)]
for (first, last) in test:
    print(first + last)
 
 
# In[ ]:
 
 
fruits = ['사과', '바나나', '딸기', '포도', '배']
for fruit in fruits:
    print(fruit)
 
 
# In[ ]:
 
 
# continue: 다음 loop로 바로 이동
fruits = ['사과', '바나나', '딸기', '포도', '배']
for fruit in fruits:
    if fruit == '바나나': continue
    print(fruit)
 
 
# In[ ]:
 
 
numbers = [1, 2, 3, 4]
result =[]
for num in numbers:
    result.append(num * 2)
print(result)
 
result = [num * 3 for num in numbers] # list comprehension
print(result)
 
 
# ### While-loop
 
# In[ ]:
 
 
i = 0
while i < 10:
    print(i)
    i += 1
 
 
# In[ ]:
 
 
# break
coffee = 10
# money = 300
while True:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
 
 
# In[ ]:
 
 
# continue
a = 0
while a < 10:
    a += 1
    if(a % 2 == 0): continue
    print(a)
 
 
# ## 3. Data Structures
# 파이썬은 tuple, list, dictionary, set 이라는 데이터 구조를 지원하고 있습니다.
 
# ### Tuple
# Tuples are read-only collections of items. (You cannot change values in a tuple!)
 
# In[5]:
 
 
a = (1, 2, 3)
print(a)
b = (1, 2, a)
print(b)
c = (1, 2, 'a')
print(c)
 
 
# In[6]:
 
 
a = (1, 2, 3, 4)
print(len(a))
print(a[0])
print(a[1])
print(a[1:3])
 
 
# In[7]:
 
 
a[2] = 'g'
 
 
# ### List
# Lists use the square bracket notation and can be index using array notation.
 
# In[8]:
 
 
a = [1, 2, 3]
b = [1, 2, a]
c = [1, 2, 'a', 'b', -3]
print(a)
print(b)
print(c)
 
 
# In[9]:
 
 
d = [1, 2, 3, ['a', 'b']]
print(d[0])
print(d[-1])
print(d[-1][0])
 
 
# In[ ]:
 
 
# 연산자
a = [1, 2, 3]
b = ['a', 'b', 'c']
print(a + b)
print(a * 3)
 
 
# In[ ]:
 
 
# Modify list
a = [1, 2, 3]
a[2] = 4
print(a)
del a[0]
print(a)
 
 
# In[ ]:
 
 
# Append a value to list
mylist = [1, 2, 3]
print("First Value: %d" % mylist[0])
mylist.append(4)
print("List Length: %d" % len(mylist))
for value in mylist:
    print(value)
 
 
# In[ ]:
 
 
# Sort a list
test = [1, 5, 3, 9]
test.sort()
print(test)
 
test = ['z', 'g', 'a', 'h']
test.sort()
print(test)
 
# Reverse a list
test.reverse()
print(test)
 
# Return index
test = [1, 2, 3, 4]
print(test.index(4))
print(test.index(0))
 
 
# In[ ]:
 
 
# in, not in
test = [1, 2, 3, 4]
print(1 in test)
print(5 in test)
print(5 not in test)
 
 
# ### Dictionary
# - key와 이에 대응하는 value를 저장해주는 자료 구조
# - 프로그래밍 언어에서 hash에 해당하는 것을 파이썬에서는 dictionary라 부름
# - {key1:value1, key2:value2, key3:value3}
 
# In[10]:
 
 
profile = {'name':'고태훈', '좋아하는 과일':'사과', '나이':34}
print(profile['name'])
print(profile['좋아하는 과일'])
print(profile['나이'])
 
# dict_keys, dict_values, dict_items는 dictionary를 위한 파이썬만의 자료구조로 list와는 다름
print(profile.keys())
# print(list(profile.keys()))
print(profile.values())
print(profile.items())
 
 
# In[ ]:
 
 
mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % mydict['a'])
mydict['a'] = 11
print("A value: %d" % mydict['a'])
print("Keys: %s" % mydict.keys())
print("Values: %s" % mydict.values())
for key in mydict.keys():
    print(mydict[key])
 
 
# In[ ]:
 
 
# get: key에 대한 value를 출력하는 방법
profile = {'name':'고태훈', '좋아하는 과일':'사과', '나이':32}
a = profile.get('키')
print(a)
# b = profile('키')
 
 
# In[ ]:
 
 
# in, not in
a = {'key1':1, 'key2':2, 'key3':3}
print('key1' in a)
print('key1' not in a)
print('key4' in a)
print('key4' not in a)
 
 
# ### Set(집합)
# - 수학에서의 "집합"과 동일한 성격
# - Set 내의 성분은 순서와 관련이 없음 (index가 없음)
# - 중복된 값을 넣을 수 없음
 
# In[11]:
 
 
# set은 {}으로 정의
# 중복된 값이 들어가면 자동으로 이를 처리함
a = {1,2,2,3,4,5}
print(a)
 
# 집합 안의 성분이 들어있는지 아닌지를 판단
print(1 in a)
print(6 in a)
 
# 공집합 만들기
empty = set()
print(empty)
 
 
# In[ ]:
 
 
a = {1,2,3}
b = {'a','b','c', 3, 4, 5}
 
# 합집합
print(a | b)
 
# 차집합
print(a - b)
print(b - a)
 
# 교집합
print(a & b)
 
# (a와 b의 합집합) - (a와 b의 교집합)
print(a ^ b)
 
 
# # 4. Function
# 함수는 프로그래밍을 더욱 아름답게 만들어줍니다.
# - 입력, 출력, 함수 세 가지 요소로 구성됩니다.
# - return은 반드시 하나만 가능합니다.
 
# In[ ]:
 
 
# Sum function
def mysum(x, y):
    return x + y
 
result = mysum(20, 30)
print(result)
 
 
# In[ ]:
 
 
# No inputs
def say():
    return('Hi!')
result = say()
print(result)
 
 
# In[ ]:
 
 
# No outputs
def say():
    print('Hi!')
say()
 
 
# In[ ]:
 
 
# input의 수를 자유롭게 설정하고 싶은 경우
def mysum(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum
result = mysum(1,2,3,4,5)
print(result)
 
 
# In[ ]:
 
 
# # 하나의 개체만 return이 됩니다.
# def calc(a,b):
#     return a + b
#     return a * b
# result = calc(1,2)
# print(result)
 
# def calc(a,b):
#     return a + b, a * b
# result = calc(1,2)
# print(result)
 
def calc_list(a,b):
    result = []
    result.append(a + b)
    result.append(a * b)
    return result
result = calc_list(1,2)
print(result)
 
 
# # Exercise 1: 소수 판별기
# - 특정 자연수를 입력으로 넣었을 때, 이 자연수가 소수(1과 자기 자신만을 약수로 갖는 수)인지 아닌지를 판별하는 함수를 만들어보세요.
# - 소수의 예: 2, 3, 5, 7, 11,...
 
# # Exercise 2: 과일가게 매출
# - 과일가게에는 3가지 종류(apple, banana, orange)의 과일을 팔고 있습니다.
# - 각 과일의 재고는 총 10개씩 있으며, 가격은 각각 1000원, 500원, 700원입니다.
# - 1) 위의 정보를 dictionary로 만들어서 모든 과일을 다 팔았을 때의 가격을 계산해보세요.
# - 2) 임의의 과일 재고 dictionary와 가격 dictionary가 입력되었을 때, 모든 과일의 가격 총합을 계산하는 함수를 만들어보세요.