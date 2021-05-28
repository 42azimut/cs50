# 공백으로 구분되어 입력되는 숫자들을 받아서 리스트 A에 저장해 보세요.

# 같은 항목이 있으면 False를, 같은 항목이 없으면 True를 반환하는 함수 unique_elements(A)를 완성해 보세요.


# 1번을 해보세요!
A = [int(x) for x in input().split(" ")]

# 2번을 해보세요!
def unique_elements(A):

	len_n = len(A)
	
	for i in range(len_n-1):
		for j in range(i + 1,  len_n):
			if A[i] == A[j]:
				return False
		
	return True
  
if __name__ == '__main__': 
# 출력합니다!
  print(unique_elements(A))