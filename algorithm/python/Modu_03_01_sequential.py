# 리스트에서 특정 숫자의 위치 찾기
# 입력: 리스트 a, 찾는값 x
# 출력: 찾으면 그 값의 위치, 찾지 못하면 -1

v = [ 17, 92, 18, 33, 58, 33, 43]

def search_list(a, x):
  n = len(a)
  for i in range(n):
    if x == a[i]:
      return i
  return -1

print(search_list(v, 33))  