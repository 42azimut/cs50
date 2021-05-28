# compute_square_C(n) 함수로 다음과 같이 n의 제곱 값이 출력되는 함수를 작성해 보세요.
#  이때, 이중 for 문을 사용하여 복잡도가 O(n²) 이 되게 작성해 보세요.

# 1번을 해보세요!
def compute_square_C(n):
    sum = 0
    # 복잡도가 O(n^2)이 되도록 이중 for 문을 작성해보세요!
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum = i * j
    return sum
    
# 2번을 해보세요!
n = int(input())

if __name__ == '__main__': 
# 출력합니다!
  print(compute_square_C(n))