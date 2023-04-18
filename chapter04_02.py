# Chapter 04-2
# For 실습

# for in <collection>
#   <loop body>

for v1 in range(10): # 0 ~ 9
    print('v1 is : ', v1)

print()

for v2 in range(1,11):
    print("v2 is : ", v2)

print()

for v3 in range(1, 11 ,3):
    print('v3 is : ', v3)

print()

# 1 ~ 1000 까지 합

sum1 = 0

for i in range(1,1001):
    sum1 += i

print('1 ~ 1000 Sum : ', sum1)

print()

print('1 ~ 1000 Sum :', sum(range(1, 1001)))

print ()

# 1 ~ 1000 까지 4의 배수의 합

print('1 ~ 1000 4의 배수 합 : ', sum(range(4,1001,4)))
print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, dict
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for name in names:
    print('You are :', name)
print()

# 예제 2 
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

# 예제 3
word = "Beautiful"

for s in word:
    print("word is :", s)

# 예제 4
my_info = dict(
    name = 'Lee',
    Age = 33,
    City = "Seoul"
)

for i in my_info:
    print('key : ', i)

print()

for k in my_info:
    print("values : ", my_info.get(k))

print()

for k in my_info:
    print("values : ", my_info[k])

print()

for v in my_info.values():
    print('values : ', v)

print()

# 예제 5

name = 'FineAppLe'
sum_name = ""

for i in name:
    if i.isupper():
        print(i)
    else:
        print(i.upper())

print()

# 문자열 합쳐서 표현
for i in name:
    if i.isupper():
        sum_name += i
    else:
        sum_name += i.upper()
       
print(sum_name)

print()

# break

numbers = [14, 3, 7, 10, 24 ,17 ,2, 15, 34, 36, 38]

for n in numbers:
    if n == 34:
        print('Found : 34!')
        break
    else:
        print('Not Found :', n)

print()

# continue

lt = ["1", 2, 5, 2, True, 4.3, complex(4)]

for i in lt:
    if type(i) is bool:
        continue
    print("current Type : ", i ,type(i))
    print("multiply by 2 : ", i * 2)

print()

# for - else / 찾았고 break문을 만났다면 else 실행하지 않음, 끝까지 찾았지만 없었으면 else 실행

numbers = [14, 3, 7, 10, 24 ,17 ,2, 15, 34, 36, 38]

for n in numbers:
    if n == 49:
        print('Found : 24')
        break
else:
    print('Not Found : 24')

print()

# 구구단 출력

for i in range(2,10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end = '')
    print()

print()

# 변환 예제

name2 = 'AceMan'
name3 = ''

print('Reverse : ', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2)))

for s in list(reversed(name2)):
    name3 += s

print('Reversed name : ', name3)

print()