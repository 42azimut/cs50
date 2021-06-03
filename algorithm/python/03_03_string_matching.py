# 1번을 해보세요!
def string_matching(T, P):
  #if len(T) >= len(P):
    
    #return T.find(P[0])   //이걸 이틀 동안 ㅠㅠ 너무해!
    return T.find(P)

# 2번을 해보세요!
T = input()
P = input()

# 출력합니다!
print(string_matching(T, P))

#문자열 매칭 문제 | p.108
# 길이가 n인 입력 문자열 T와 길이가 m인 패턴 문자열 P가 있습니다.

# 항상 n >= m이라고 가정합니다.
# 모든 문자열은 알파벳과 띄어쓰기만으로 구성되어 있다고 가정합니다.
# 대문자와 소문자를 구분합니다. 예를 들어, ‘a’와 ‘A’를 다른 문자로 취급합니다.
# T에서 가장 먼저 나타나는 P의 위치를 찾아봅시다. 패턴이 없으면 -1을 반환합니다.

# 이렇게 해보세요!
# 책 p.108~111을 참고해서 풀어보세요!

# T에서 가장 먼저 나타나는 P의 위치를 찾으면 그 인덱스를 반환하고, 패턴이 없으면 -1을 반환하는 함수 string_matching(T, P)을 완성해 보세요.
# 입력 문자열 T와 패턴 문자열 P를 입력받아 보세요.

# 입력 예시
# BRUTEFORCE
# FOR

# 출력 예시
# 5