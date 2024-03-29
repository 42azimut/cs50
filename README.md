- [react ReadME](https://github.com/42azimut/cs50/blob/master/algorithm/javascript/react_README.md)
- [python alogorithm](https://github.com/42azimut/cs50/blob/master/algorithm/python/python_algo_README.md)
- [코딩 앙마 리액트](https://www.youtube.com/watch?v=05uFo_-SGXU&list=PLZKTXPmaJk8J_fHAzPLH8CJ_HO_M33e7-)

## Lama Dev
- [React Node.js Social Media App Tutorial - MERN Stack App Full Course w/ Hooks - Context API](https://www.youtube.com/watch?v=pFHyZvVxce0&t=134s)
- [React Node.js Full Stack Blog App Tutorial | MERN Stack APP Full Course](https://www.youtube.com/watch?v=LelifxOrzvw)

##  cs50
- Harvard University CS50 

___
## 자바스크립트 
### 06_08 JSON.stringify
- 자바스크립트 객체를 JSON 문자열로 변환할 때는 JSON.stringify() 메소드를 사용합니다.

### 06_09 JSON.parser
- JSON 문자열을 자바스크립트 객체로 전개할 때는 JSON.parse() 메소드를 사용합니다. 매개변수에 JSON 형식의 문자열을 넣어주면 됩니다.

### 06_12 lodash 라이브러리> _.sortBy() 메서드
- dash == -
- lodash == low dash == _  (under score)
- Lodash 라이브러리는 _라는 이름의 객체 안에 수많은 메소드를 담고 있습니다. _라는 이름 때문에 조금 당황할 수도 있습니다. 자바스크립트는 _와 $ 기호를 식별자로 사용할 수 있는데, 이때 _기호를 사용해서 식별자를 만들었을 뿐입니다. sortBy() 메소드는 배열을 어떤 것으로 정렬할지 지정하면, 지정한 것을 기반으로 배열을 정렬해서 리턴해주는 메소드입니다.

### 06 mission Math sin(90) 으로 1 만들기
- 단순구현 하면 0.89..... 나온다
` Math.sin(90 * Math.PI / 180.0)`


### 07_26 글자 수 출력하기
- focus : 입력양식 활성화
- blur : 입력양식 비활성화
- 아시아권의 문자는 키보드 이벤트(keydown, keypress, keyup 이벤트)로 원하는 것을 제대로 구현할 수 없는 경우가 많습니다. 본문에서 살펴보았던 남은 글자 수 세기 프로그램도 문제가 있다고 언급했습니다.

- 실제로 트위터는 다음과 같이 타이머를 사용해서 50밀리 초마다 입력 양식 내부의 글자를 확인해서 글자 수를 셉니다. focus 이벤트와 blur 이벤트를 사용했는데요. 이 이벤트는 입력 양식에 초점을 맞춘 경우(활성화 상태)와 초점을 해제한 경우(비활성화 상태)에 발생하는 이벤트입니다. 입력 양식에 글자를 입력하려고 선택한 순간부터 타이머를 돌리고, 다른 일을 하기 위해서 입력 양식에서 초점을 해제하면 타이머를 정지하게 만든 것입니다.

어떤 상황에서도, 어떤 언어를 입력하더라도 글자 수를 정상적으로 출력하도록 작성한 코드입니다.


### 07_27 웹 브라우저에 데이터를 저장하는 localStorage 객체와 활용하기

- localStorage 객체는 웹 브라우저가 기본적으로 제공하는 객체입니다. 이 객체는 다음과 같은 메소드를 갖고 있습니다.
  - **localStorage.getItem(키)**: 저장된 값을 추출합니다. 없으면 undefined가 나옵니다. 객체의 속성을 추출하는 일반적인 형태로 localStorage.키 또는 localStorage[키] 형태로 사용할 수도 있습니다.
  - **localStorage.setItem(키, 값)**: 값을 저장합니다. 이전과 마찬가지로 객체에 속성을 지정하는 일반적인 형태를 사용할 수도 있습니다.
  - **localStorage.removeItem(키)**: 특정 키의 값을 제거합니다.
  - **localStorage.clear()**: 저장된 모든 값을 제거합니다.

- 참고해주세요!
  - 코드를 실행하면 처음에는 입력 양식이 비어있습니다. 글자를 입력하고 화면을 새로 고침해보세요. 지금까지 살펴본 프로그램들은 화면을 새로 고침하는 순간 입력한 내용이 모두 사라졌지만, 여기서는 입력값이 그대로 남아있는 것을 확인할 수 있습니다.


### 09_14 private 속성 사용하기(1)
-  클래스 사용자가 클래스 속성(또는 메소드)을 의도하지 않은 방향으로 사용하는 것을 막아 클래스의 안정성을 확보하기 위해 나온 문법이 private 속성과 메소드입니다. 문법은 다음과 같습니다.

- 속성과 메소드 이름 앞에 #을 붙이기만 하면 됩니다. 이처럼 #이 붙어있는 속성과 메소드는 모두 private 속성과 메소드가 됩니다. 주의할 것이 있다면 private 속성은 사용하기 전에 미리 외부에 어떤 속성을 private 속성으로 사용하겠다고 선언해줘야 한다는 것입니다.

### 9_15 private 속성 사용하기(2) | p.411
- 이렇게 private 속성으로 변경하면 클래스 외부에서는 해당 속성에 접근할 수 없습니다. 예를 들어 square 객체의 length 속성을 변경해보겠습니다. 변경해도 클래스 내부에서 사용하고 있는 속성은 #length 속성이지 length 속성이 아니므로 결과에는 어떠한 영향도 주지 않습니다.

### 9-16 private 속성 사용하기(3) | p.411
- #length 속성을 사용하면 다음과 같은 오류를 발생합니다.
`Uncaught SyntaxError: Private field '#length' must be declared in an enclosing class`

- 이렇게 만든 private 속성은 클래스 외부에서는 접근할 수 없으므로 클래스 사용자가 클래스를 잘못 사용하는 문제를 줄일 수 있습니다.
