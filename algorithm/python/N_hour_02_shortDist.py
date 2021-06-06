# 1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오. 
# (단 점들의 배열은 모두 정렬되어있다고 가정한다.)

# 예를들어 S={1, 3, 4, 8, 13, 17, 20} 이 주어졌다면, 결과값은 (3, 4)가 될 것이다.

# s =  [1, 3, 4, 8, 13, 17, 20]
# max_s = max(s)
# print(max_s)

# index = 0
# for i in range(len(s) - 1):
#   if max_s > s[i+1] - s[i]:

s =  [1, 3, 4, 8, 13, 17, 20]
ss = [3, 4, 8, 13, 17, 20]   # 짝지어 정렬

#  가장 많이 사용! 매우 중요 람다!
print(list(zip(s, ss)))
print(sorted(list(zip(s, ss)), key=lambda i : i[1]))  # i[1] 묶임 값에서 뒤에 값(1번째)을 기준으로 정렬!
print(sorted(list(zip(s, ss)), key=lambda i : i[1] - i[0])[0])   # 값의 차에서 첫번째 원소( 가장 작은 값)


#함수 만들어서 적용! but 재사용성 없음! 잘 사용 안함!
def defer_nums(i):
  return i[1] - i[0] 
print(sorted(list(zip(s, ss)), key= defer_nums)[0]) 