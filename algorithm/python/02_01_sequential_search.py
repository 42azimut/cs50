# 탐색 대상인 리스트 A의 모든 항목을 순서대로 key와 비교하여 같으면 그 위치(인덱스)를 반환하고, 찾으려는 key 값이 리스트 A에 없으면 -1을 반환하는 순차 탐색 함수 sequential_search(A, key)를 완성해 보세요.
# 리스트 A와 탐색 키 key를 입력받아 보세요. 입력은 아래 예시와 같이 주어져요.

# 입력 예시

# 32 14 5 17 23 9 11 4 26 29
# 32
# Copy
# 가장 첫 줄에는 리스트 A에 들어가는 숫자들이 공백으로 구분되어 입력돼요.
# 두 번째 줄에는 key의 값이 입력돼요.

# 출력 예시

# 32찾기: 0

# 1번을 해보세요!
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1		

# 2번을 해보세요!
A = [int(x) for x in input().split()]
key = int(input())

if __name__ == '__main__': 
# 출력합니다!
  print("%d찾기:" %(key), sequential_search(A, key))