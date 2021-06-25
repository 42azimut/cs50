/* eslint-disable */

import React, { useState } from 'react';
import './App.css';


function App() {

  let [글제목, 글제목변경] = useState(['남자aaa 코트 추천', '송파 aaaa스테이크', 'Python Djsngo studying']); // [state 데이터, state 데이터 변경 함수]
  let [like, likeUpdate] = useState(0);
  let posts = '강남 고기 맛집';

  // function titleUpdate() {
  //   let newArr = [...글제목];   //deep copy
  //   newArr[0] = '여자코트 추천'
  //   글제목변경(newArr)
  // }
  


  return (
    <div className="App">
      <div className="black-nav">
        <div>개발 블로그</div>
      </div>

      <Modal></Modal>

      <div className="list">
        <h3> { 글제목[0] } <span onClick={ () => { likeUpdate( like + 1) } }>❤️</span> { like } </h3>
        <p>6월 25일 발행</p>
        <hr/>
      </div>

      <div className="list">
        <h3>{ 글제목[1] }</h3>
        <p>3월 22일</p>
        <hr />
      </div>

      <div className="list">
        <h3>{ 글제목[2] }</h3>
        <p>12월 26일</p>
        <hr />
      </div>
    </div>
  );
}

function Modal() {   
  return (
    <div className="modal">
      <h2>제목 modal</h2>
      <p>날짜</p>
      <p>상세 내용</p>
  </div>
  )
}

export default App;