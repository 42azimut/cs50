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

``
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
 
