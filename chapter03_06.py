# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서 X, 중복X)

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'qux'} # 키와 밸류가 존재하지 않고 컴마로 이루어져있으면 set 자료형
f = {42, 'foo', (1,2,3), 3.1415}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)
print()

# 튜플 변환 (set => tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환 (set => list)
l = list(c)
l2 = list(e)

print('l - ', type(l), l)
print('l2 - ', type(l2), l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s3 = set([1,2,3])

print('s1 & s2', s1 & s2) # 교집합
print('s1 & s2', s1.intersection(s2))

print('s1 | s2', s1 | s2) # 합집합
print('s1 | s2', s1.union(s2))

print('s1 - s2', s1 - s2) # 차집합
print('s1 - s2', s1.difference(s2))

# 중복 원소 확인 (False가 중복, True가 중복 아님)
print('s1 & s2 :', s1.isdisjoint(s2)) # False가 나오면 교집합 되는 원소가 있다는 뜻

# 부분 집합 확인
print('subset : ', s1.issubset(s2))
print('subset : ',s1.issubset(s3))
print('subset : ',s3.issubset(s1))
print()
print('superset : ',s1.issuperset(s2))
print('superset : ',s3.issuperset(s1))
print('superset : ',s1.issuperset(s3))

# 추가 & 제거
s1 = set([1,2,3,4])

s1.add(5)
print('s1 - ', s1)
s1.remove(2)
print('s1 - ', s1)

# 없는 값을 remove 메서드를 이용해 삭제하려하면 키 에러
#s1.remove(10)

s1.discard(3)
print('s1 - ', s1)

# discard는 없는 값을 삭제하려해도 에러가 발생하지 않는다.
s1.discard(8)
print('s1 - ', s1)

# 전부 삭제
s1.clear()
print('s1 - ', s1)