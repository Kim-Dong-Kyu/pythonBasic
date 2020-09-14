# 문자열 인덱스
#  문자열 순서별로 인덱스를 가지고 있음

text = 'abc'

print(text[0])
print(text[1])
print(text[2])

print(text[-3])
print(text[-2])
print(text[-1])

# 원하는 구간 문자열 출력 문자열 슬라이스

text ="kim-dong-kyu"
print(text[0:3])
print(text[2:5:2]) # 마지막 인수는 간격을 의미한다
print(text[0:8:2])


print(text[::-1]) # 문자열을 뒤집는다 



