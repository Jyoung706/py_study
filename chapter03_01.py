# Chapter 03-1
# 숫자형

# 파이썬 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = True
str2 = "Anaconda"
float_v = 10.0 # 10 int == 10.0 float -> false
int_v = 7
list = [str1, str2] # 자스에서 배열
dict = { # 자스에서 객체 / 키와 값으로 이루어짐
    "name" : "Machine Learning",
    "version" : 2.0
}
tuple = (7, 8, 9)
set = {3, 6, 9}

# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float_v))
print(type(int_v))
print(type(list))
print(type(dict))
print(type(tuple))
print(type(set))

# 숫자형 연산자
'''
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x, y), x ** y : x 의 y 제곱
'''

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777777777799999999999999999999999999999999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3/9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습

i1 = 39
i2 = 939
big_int1 = 7777777777777777777777999999999999999999999999999324
big_int2 = 6666666666666666455555555555555555455555555555555556
f1 = 1.234
f2 = 3.324

# +
print('{:>>10s}'.format('+'))
print("i1 + i2 : ", i1 + i2)
print("big_int1 + big_int2 : ", big_int1 + big_int2)
print("i1 + f1 : ", i1 + f1) # i1 은 정수 f1 은 실수 print 결과는 40.234로 자동으로 형변환이 된다.
print()

# *
print('{:>>10s}'.format('*'))
print("i1 * i2 : ", i1 * i2)
print("big_int1 * big_int2 : ", big_int1 * big_int2)
print("i1 * f1 : ", i1 * f1)
print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

# 타입 출력
print(type(a), type(b), type(c), type(d))
print()

# 형 변환
print(float(b))
print(int(a))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0
print(int(False))
print(float(True))
print(float(False))
print(complex(3))
print(complex('3')) # 문자형 => 숫자형
print(complex(False))
print(complex(True))
print()

# 수치연산 함수
print(abs(-7))
x, y = divmod(100, 8) # x 는 몫, y 는 나머지

print('x :', x,'y :', y)
print(pow(5,3), 5 ** 3)
print()

# 외부 모듈
import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
print(math.pi)