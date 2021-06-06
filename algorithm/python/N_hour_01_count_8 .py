# 1번 워밍업 문제(구글)
# 1부터 10,000 까지 8이라는 숫자가 총 몇번 나오는가?

# 8이 포함되어 있는 숫자의 개수를 카운팅 하는 것이 아니라, 8이라는 숫자를 모두 카운팅 해야 한다.
# 예: 8808은 3, 8888은 4로 카운팅
# 문제링크 : https://codingdojang.com/scode/393

# result = str(list(range(1, 10001))).count('8')
# print(result)

count = 0
for i in range(10001):
  if '8' in str(i):   # count() 메서드 사용하기 위해 문자열로 변환!
    count += str(i).count('8')
print(count)