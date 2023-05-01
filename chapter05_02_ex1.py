# Chapter05-2-ex1
# 파이썬 사용자 입력

# 예제1 => 예외 처리
""" try:
    n = int(input("Enter a number : "))
    print("OK. Your Number is : ", n)
except ValueError:
    print("This is not a number") """

# 예제2 => 올바른 값 입력 완료까지 지속
while True:
    try:
        n = int(input("Enter a number : "))
        print("OK. Your Number is : ", n)
        break
    except ValueError:
        print("This is not a number")