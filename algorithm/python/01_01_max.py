# 이렇게 해보세요!
# 책 p.24를 참고해서 풀어보세요!

# 리스트 A의 모든요소들 중 최댓값을 찾아 return 하는 함수 find_max( A )를 완성해 보세요.
# 공백으로 구분되어 입력되는 숫자들을 받아서 array에 저장해 보세요.

# 입력 예시
# 20 34 12 93 84 39 64 55 24

# 출력 예시 
# [20, 34, 12, 93, 48, 39, 64, 55, 24] 최댓값= 93


# 1번을 해보세요!
def find_max( A ): 
    return max(A)

# 2번을 해보세요!
array = [int(x) for x in input().split()]

if __name__ == '__main__':  
  print(array, "최댓값=", find_max(array))


