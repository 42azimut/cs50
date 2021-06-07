# 비밀지도

# bin(), oct(), hex()

# a = bin(30)
# print(a)

b = bin(9 | 30)[2:].replace('1', '#').replace('0', ' ')
print(b)

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5

print('zip으로 묶고 unpacikng i, j')
for i, j in zip(arr1, arr2):
  print(i, j)   # unpacking (i, j)

#단 위에서 자리수를 맞춰야 한다. 
# (3,5)이면 아래와 같이 나온다.  따라서 zfill(n) 5자리에 0으로 채움!
#  ###
#  # # #  
print('bin 이진화 만들고, 자리수 채우기')
for i, j in zip(arr1, arr2):
  print(bin(i | j)[2:].zfill(10))


print('맞춤 코드')
for i, j in zip(arr1, arr2):
  print(bin(i | j)[2:].zfill(n).replace('1', '#').replace('0', ' ')
)

print('final 솔루션')
def solution(n, arr1, arr2):
  answer = []
  for i, j in zip(arr1, arr2):
    answer.append(bin(i | j)[2:].zfill(n).replace('1', '#').replace('0', ' '))
  return answer
print(solution(n, arr1, arr2))