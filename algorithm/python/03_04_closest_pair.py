# 필요한 모듈을 추가해 보세요!
import math


# 1번을 해보세요!

# def get_x_y(p):
#   x = []
#   y = []
#   for i in range(len(p)):
#     x.append(p[i][0])
#     y.append(p[0][i])
  
#   x_dist = math.pow()
#     return x, y

def closest_pair(p):
  get_x_y(p)




# 2번을 해보세요!
# p = list(tuple(map(int,input().split())) for r in range(int(input('enter num of rows : '))))
p = list(tuple(map(int, input().split())) for r in range(int(input('입력값: '))))


if __name__ == '__main__': 

  #print(p)
  # 출력합니다!
  print("최근점 거리:", closest_pair(p))


# 최근접 쌍의 거리 문제 | p.112
# 2차원 평면상에 n개의 점이 있습니다. 가장 인접한 쌍의 거리를 구해봅시다.

# 두 점 사이의 거리를 계산할 때는 유클리드 거리(Euclidean distance)를 이용합니다.
# 유클리드 거리를 구할 때 math 모듈의 sqrt()와 거듭제곱 연산자를 사용해 봅시다.
# 이렇게 해보세요!
# 책 p.112~115를 참고해서 풀어보세요!

# 가능한 모든 점의 쌍에 대해 거리를 계산하고 가장 짧은 것을 찾는 함수 closest_pair(p)를 완성해 보세요. 
# 코드가 너무 길어진다면 추가적인 함수를 정의하여 closest_pair(p) 내에서 호출해도 좋아요.
# 점의 리스트 p를 입력받아 보세요. p는 [(x1, y1), …, (xn, yn)] 의 형태로 되어 있으며, 입력은 아래 예시와 같이 주어져요.

# 입력 예시
# 6
# 2 3
# 12 30
# 40 50
# 5 1
# 12 10
# 3 4

# 출력 예시
# 최근접 거리: 1.4142135623730951

# 가장 첫 줄에는 p에 들어가는 점의 쌍 개수가 주어져요. 두 번째 줄부터 한 줄마다 한 튜플 내에 들어가는 
# 두 개의 숫자가 공백으로 구분되어 주어져요.
# 위와 같은 입력이 주어진다면 p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]의 형태로 구성되어야 해요.

# 튜플로 이루어진 리스트 p를 입력받아 보세요.

# 참고해주세요!
# 파이썬에서 무한대의 실숫값을 원한다면 다음과 같은 코드를 사용할 수 있어요.

# INF = float('Inf')   # 가장 큰 가중치 (실수 무한대)
# Copy
# import sys
# INF = sys.maxsize   #가장 큰 가중치 (정수 무한대)