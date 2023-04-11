#chapter 02 - 1
#print 사용법

#기본 출력
print('Python Start!')
print("Python Start!")
print()
print()
print('''Python Start!''')
print("""Python Start!""")

print()

#seperator 옵션

print('P', 'Y', 'T', 'H', 'O', 'N', sep='')

print('010', '7877', '1234', sep='-')
print('python', 'google.com', sep='@')

print()

#end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

print()

#file 옵션 => 파일에 쓸 때

import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 정수, s : 문자열 , f : 실수)
# d : 3, s : 'python', f : 3.141592

print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two')) # 0과 1은 index

# %s 사용법
print('%10s' %('nice11')) #문자열 10글자를 부여하는데 부여된 문자열이 10글자가 아닐 경우 왼쪽부터 공백으로 채움
print('{:>10}'.format('nice11')) # {} expression 에서는 s를 안붙여도 상관없지만 d나 f는 {} expression 에서는 명시적으로 붙여줘야 한다.

print('%-10s' %('nice11')) #문자열 10글자 부여하는데 왼쪽부터 부여 안채워진 부분은 공백
print('{:10}'.format('nice11'))

print('{:_>10}'.format('nice11')) #부여되지 않은 부분을 내가 넣고싶은 기호로 넣는다.
print('{:^10}'.format('nice11')) #중앙 정렬

print('%.5s' %('nice'))
print('%.5s' %('pythonstudy')) # 5글자 초과하면 5글자만 출력
print('%5s' %('pythonstudy')) # 5글자 초과하더라도 다 출력
print('{:10.5}'.format('pythonStudy'))

print()

# %d
print('%d %d' %(1,2))
print('{} {}'.format(1,2))
print('{1} {0}'.format(2,1))

print('%4d' %(42))
print('{:4d}'.format(42))

# %f

print('%f' %(3.1311414141414123123))
print('{:f}'.format(3.131141414141414144))
print('%1.2f' %(3.14))
print('{:1.2f}'.format(3.14))

print('%06.2f' %(3.141592653589793)) #소수부에서는 자릿수 생각을 해야함 , 06은 전체 자릿수 .2f 는 뒤에 소수점 두자리
print('{:06.2f}'.format(3.141592653589793))