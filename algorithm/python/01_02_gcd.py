# 두 자연수 a와 b의 최대 공약수(Greatest Common Divisor)를 구해봅시다. a와 b의 최대 공약수는 a의 약수인 동시에 b의 약수인 숫자 중에서 가장 큰 수를 의미합니다.

# 유클리드 알고리즘(Euclid’s algorithm)을 이용해 풀어봅시다.

# a와 b의 최대 공약수 gcd(a, b)를 구하기 위해 아래와 같은 정리를 이용합니다. 이때, 반드시 a가 b보다 작지 않아야 합니다.
# gcd(a, b) = gcd(b, a mod b)

# 이렇게 해보세요!
# 책 p.27을 참고해서 풀어보세요!

# a와 b에 저장될 자연수가 한 줄에 하나씩 주어집니다. 이때, a는 b보다 작지 않습니다. 값을 받아서 a와 b에 각각 저장해 보세요.
# 입력 예시

# 60
# 28
# Copy
# 자연수 a와 b의 최대공약수를 return 하는 함수 gcd(a, b)를 완성해 보세요.
# 출력 예시

# 60, 28의 최대 공약수 = 4

# 1번을 해보세요!
a = int(input())
b = int(input())

# 2번을 해보세요!
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
if __name__ == '__main__':  
# 출력합니다!
  print("%d, %d의 최대 공약수 =" % (a, b), gcd(a, b))