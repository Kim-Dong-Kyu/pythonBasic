# 리스트는 [] 로 둘러 쌓여 있지만 튜플은 () 둘러싼 배열 
# 수정이 불가능

t1 = (1,2,'a','b')
del t1 [0]

# -> 오류를호출 튜플의 데이터는 변경할 수 없기 때문에