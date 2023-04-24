# Chapter05-0
# 함수란? 완전 함수 기초 설명

# 에제 1 : 매개변수가 필요하지 않은 함수 리턴 없음
def function():
    print('예제1 호출')

# 예제2 : 매개변수가 필요한 함수 리턴 없음

def function2(a, b):
    print('예제2 호출', a,b)

# 예제3 : 결과값 반환X
def function3(x,y):
    print('예제3 호출', x,y)

# 예제3 : 결과값 반환O
def function4(x,y):
    return x + y

# 실행

function()
function2(10, 30)
function3(100,300)
print('예제4 호출' ,function4(1,2))

r = function4(50,5000)
print('예제4 호출',r)