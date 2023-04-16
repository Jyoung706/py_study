# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자열 생성
str1 = "I am Python"
str2 = "Python"
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자 사용 (\ 뒤의 특수기호는 그대로 출력)
# I'm Boy
"""
참고 : Escape 코드

\n : 개행
\t : 탭의 넓이만큼 띄운다.
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
"""

print("I'M Boy")
print('I\'m Boy')
print('I\\m Boy')
print()
print('a\tb')
print('a\nb')
print("a\"\"b")
print ()

escape_str1 = "Do you have a \"retro games?\""
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)
print()

# 탭, 줄 바꿈

t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s1 = r'D:\python\test'
print(raw_s1)
print()

# 멀티라인 입력
# 역슬래쉬 사용해라
multi_str = '''
String
Multi Line
Test
'''
print(multi_str)
print()

multi_str2 = \
'''
문자열
멀티라인
테스트
'''
print(multi_str2)
print()

multi_str3 = \
'asdf' \
'aavbb' \
'asdf'

print(multi_str3)
print()

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('z' in str_o1)
print('p' not in str_o2)
print('P' not in str_o2)
print()

# 문자열 형 변환
string_number = str(66)

print(string_number, type(string_number))
print(str(10.1))
print(str(True), type(str(True)))
print()

# 문자열 함수(upper, isalnum, startswith, count, endwith, isalpha...)

# 첫번째 문자 대문자
print("Capitalize : ", str_o1.capitalize())
print("str_o2 endswith? : ", str_o2.endswith("s"))
print("str_o2 endswith? : ", str_o2.endswith("e"))
print("replace : ", str_o1.replace("thon", " Good"))
print("sorted : ", sorted(str_o1))
print("split : ", str_o4.split(' '))
print()

# 반복(시퀀스)
im_str = "Good Boy!"

print(dir(im_str)) # __iter__
print()

#출력
for i in im_str:
    print(i)
print()
# 슬라이싱
str_sl = "Nice Python"

# 슬라이싱 연습
print(str_sl[0:3]) # 3 -1 까지 나옴 즉 0, 1, 2 까지 나온다.
print(str_sl[5:11])
print(str_sl[5:]) # [5:11] 과 같다
print(str_sl[:len(str_sl)]) # str_sl[:11]
print(str_sl[:len(str_sl) - 1]) # str_sl[:10]
print(str_sl[1:4:2]) # 1부터 3까지 가져오는데 두칸 단위로 가져와라
print(str_sl[1:11:2])
print(str_sl[-5:])
print(str_sl[1:-2])
print(str_sl[::2])
print(str_sl[::-1])
print()

# 아스키 코드

a = 'z'
print(ord(a))
print(chr(122))