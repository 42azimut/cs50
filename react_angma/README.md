# 코딩 앙마 React App

## 01. 소개

## 02. 설치

## 03. 컴포넌트, jsx

## 04. 첫 컴포넌트 만들기

## 05. css 작성

## 06. 이벤트 처리(Handling Events)

## 07. state, useState

## 08. props

## 09. 더미(dummy) 데이터 구현, map()반복문

## 10. 라우터 구현

## 11. json-server, REST API
- `npm i -g json-server`
- `json-server --watch ./src/db/data.json --port 3001`
- rest API : URI주소 와 메서드로 CRUD 요청하는 것!
- POST, GET, PUT, DELETE

## 12. useEffect, fectch() 로 API 호출
- 어떤 상태 값이 바꼈을때 동작하는 함수를 작성할수 있다. 
- 렌더링 후 호출된다.

```
useEffect(() => {
  fetch("http://localhost:3000/days")
    .then(res => {
      return res.json();
    })
    .then(data = > {
      setDays(data);
      });
}, []);
      
```

- useEffect를 작고 단순한 단일 목적의 함수로 분리한다면 의도치 않은 이펙트 함수의 실행을 방지할 수 있다. 물론 디펜던시 배열도 사용해야 한다.
- 커스텀 훅으로 만든다면 두 상태 변수를 완전히 독립적으로 만들 수 있다. 그리고 이 방법은 각 함수들이 어떤 변수를 사용하는지도 쉽게 파악할 수 있다.
- useEffect 안에서 사용하는 모든 변수들을 디펜던시 배열에 추가한다
- 매우 중요한 규칙이다. 앱이 점점 커질질수록 useEffect에는 더 많은 디펜던시가 추가될 수 있다. 모든 디펜던시의 변화를 감지해 깨진 클로저가 만들어지는 것을 피하려면 모든 디펜던시를 디펜던시 배열에 추가해야 한다.(이 주제에 관한 공식 문서)




 
