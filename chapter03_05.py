# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형 (순서X, 키 중복X, 수정O, 삭제O)

# 선언
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '940706', 'address' : 'Seoul'}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 30,
    'Grade' : 'A',
    'Status' : True
}

e = dict([
    ( 'Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 30),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 출력
print('a - ', a['name'])
print('a - ', a.get('name'))

# print('a - ', a['name1']) # bracket Notation으로 접근 시 없는 키에 접근 할 경우 에러가 난다.
print('a - ', a.get('name1')) # get 메서드 사용해서 접근 할 때는 없더라도 None을 반환하므로 안정적이다.
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('Name'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['Gender'] = 'Man'
print('a - ', a)
a['Rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 수정
a['name'] = 'Park'
print('a - ', a)
print()
# 딕셔너리 함수 => dict_keys, dict_values, dict_items : 반복문(__iter__) 에서 사용 가능

print('a - ', a.keys())
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys()))
print('b - ', list(b.keys()))

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())
print('a - ',list(a.values()))
print('b - ',list(b.values()))
print('c - ',list(c.values()))

print('a - ', a.items())
print('a - ',list(a.items()))

print()

print('a - ', a.pop('name'))
print('a - ', a)
print()

print('c - ', c.pop('arr'))
print('c - ', c)
print()

print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a)
print('d - ', 'birth' in d)

# 수정
a['birth'] = '880808'
print('a - ', a)

a.update(birth = '112233')
print('a - ', a)

temp = dict(
    address = 'Busan'
)

a.update(temp)
print('a - ', a)