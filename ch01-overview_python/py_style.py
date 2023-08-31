import os

for i in range(10):
    print(f"{i=}")
    print("test1")

for x in "abcdefg":
    print(f"{x=}")

# 이것은 테스트 함수 입니다.
def test_func(a):
    print(f"{type(a)}")

"""
멀티라인 문자열로 써주기도 합니다. 
특정 모듈은 포맷을 맞추면 API 문서로 변환도 해줍니다
"""
def Test_func(a):
    print(f"{type(a)=}")


test_func("A")
Test_func("a")

a = 1
print(f"{a=}")