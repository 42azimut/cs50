##  cs50
- Harvard University CS50 

___
##  python 알고리즘 - 자료구조
- 엘리스 아카데미
- 선택 정렬 : (오름차순 정렬) => 전체 리스트 탐색 -> 가장 작은 수를 맨 앞으로, 기존 원소는 서로 자리 교환!  -> 반복!!! 

___
##  Python 제주코딩베이스 캠프 - N시간만에 끝내는 코딩테스트
1.
2. [2018 카카오 코딩 테스트](https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/)
문제 설명
  
(1) 비밀 지도(난이도: 하)

네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

1) 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 “공백”(“ “) 또는 “벽”(“#”) 두 종류로 이루어져 있다.
2) 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 “지도 1”과 “지도 2”라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
3) “지도 1”과 “지도 2”는 각각 정수 배열로 암호화되어 있다.
4) 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.

### 입력 형식
- 입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

  - 1 ≦ n ≦ 16
  - arr1, arr2는 길이 n인 정수 배열로 주어진다.
  - 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2^n – 1을 만족한다.

### 출력 형식
- 원래의 비밀지도를 해독하여 "#", 공백으로 구성된 문자열 배열로 출력하라.
___

(2) 다트게임
카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다. 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.
갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다. 다트 게임의 점수 계산 로직은 아래와 같다.

1) 다트 게임은 총 3번의 기회로 구성된다.
2) 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
3) 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수^1 , 점수^2 , 점수^3 )으로 계산된다.
4) 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
5) 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
6) 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
7) 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
8) Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
9) 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

### 입력 형식
“점수|보너스|[옵션]”으로 이루어진 문자열 3세트.

예) 1S2D*3T

  - 점수는 0에서 10 사이의 정수이다.
  - 보너스는 S, D, T 중 하나이다.
  - 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

### 출력 형식
3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.

예) 37




___
## 자바스크립트 

### 07_27 웹 브라우저에 데이터를 저장하는 localStorage 객체와 활용하기

- localStorage 객체는 웹 브라우저가 기본적으로 제공하는 객체입니다. 이 객체는 다음과 같은 메소드를 갖고 있습니다.
  - **localStorage.getItem(키)**: 저장된 값을 추출합니다. 없으면 undefined가 나옵니다. 객체의 속성을 추출하는 일반적인 형태로 localStorage.키 또는 localStorage[키] 형태로 사용할 수도 있습니다.
  - **localStorage.setItem(키, 값)**: 값을 저장합니다. 이전과 마찬가지로 객체에 속성을 지정하는 일반적인 형태를 사용할 수도 있습니다.
  - **localStorage.removeItem(키)**: 특정 키의 값을 제거합니다.
  - **localStorage.clear()**: 저장된 모든 값을 제거합니다.

- 참고해주세요!
  - 코드를 실행하면 처음에는 입력 양식이 비어있습니다. 글자를 입력하고 화면을 새로 고침해보세요. 지금까지 살펴본 프로그램들은 화면을 새로 고침하는 순간 입력한 내용이 모두 사라졌지만, 여기서는 입력값이 그대로 남아있는 것을 확인할 수 있습니다.