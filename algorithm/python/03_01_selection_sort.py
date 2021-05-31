# 1번을 해보세요!
def selection_sort(A):
    # 여기에 코드를 작성해보세요!
    n = len(A)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]     
        printStep(A, i+1)
    return A
    
def printStep(arr, val):
    print("  Step %2d = " %val, end='')
    print(arr)

# 2번을 해보세요!
A = [int(x) for x in input().split()]

if __name__ == '__main__': 
# 출력합니다!
    print("Original  :", A)
    selection_sort(A)
    print("Selection :", A)

# 정렬 문제 | p.100
# 리스트에 n개의 항목이 들어 있습니다. 이들을 키(key)의 순서에 따라 
# 오름차순(non-decreasing order)으로 재배치해봅시다.

# 설명을 단순화하기 위해 항목 자체가 키값이라고 해봅시다. 여기서는 리스트에 숫자가 들어 있고, 
# 이 리스트를 오름차순으로 정렬한다고 가정합니다.

# 이렇게 해보세요!
# 책 p.100~104를 참고해서 풀어보세요!

# 제자리 정렬로 개선된 선택 정렬 알고리즘을 구현한 함수 selection_sort(A)를 완성해 보세요.
# 내부 루프의 최소 항목을 찾는 범위와 리스트의 두 항목을 서로 교환하는 코드에 유의하며 작성해 보세요.
# selection_sort(A) 함수 내에서 중간과정을 출력하는 함수 printStep(arr, val)을 호출해 선택 정렬의 전체 과정을 출력해 보세요.
# 공백으로 구분되어 입력되는 숫자들을 받아서 리스트 A에 저장해 보세요.

# 입력 예시
# 5 3 8 4 9

# 출력 예시
# Original  : [5, 3, 8, 4, 9]
#   Step  1 = [3, 5, 8, 4, 9]
#   Step  2 = [3, 4, 8, 5, 9]
#   Step  3 = [3, 4, 5, 8, 9]
#   Step  4 = [3, 4, 5, 8, 9]
# Selection : [3, 4, 5, 8, 9] 
