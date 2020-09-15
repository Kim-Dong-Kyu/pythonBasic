# 연관 배열, key value 로 되어 있는  hash 라고 생가하면 된다 

dic = {'name' : 'Kinm-Dong-Kyu' , 'phone' : '010-5044-2318', 'birth' : '951013'}
print (dic)

# 딕셔너리에 쌍 추가하기 

a = {1: 'a'}
a[2] = 'b'
print(a)

# 딕셔너리 관련 함수들 

myprofile = {'name' : 'Kinm-Dong-Kyu' , 'phone' : '010-5044-2318', 'birth' : '951013'}
print(myprofile.keys())  # 딕셔너리 키만 모아서 보여준다 
print(list(myprofile)) # 딕셔너리의 키 값을 리스트로 변환한다 


#myprofile.clear() # key : vlaue 쌍 모두 지우기 
myprofile.get('birth') # key 값을 통해 vlaue 값 받아오기

print('name' in myprofile) # 해당 키값이 딕셔너리 안에 있는지 조회한다 있으면 true 없으면 false 
