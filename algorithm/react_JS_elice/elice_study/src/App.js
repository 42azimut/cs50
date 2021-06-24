import React, { useState } from 'react';
import './App.css';


function App() {

  let [글제목, 글제목변경] = useState(['남자aaa 코트 추천', ['송파 aaaa스테이크']]); // [state 데이터, state 데이터 변경 함수]
  let [like, likeUpdate] = useState(0);
  let posts = '강남 고기 맛집';

  
  return (
    <div className="App">
      <div className="black-nav">
        <div>개발 블로그</div>
      </div>
      <div className="list">
        <h3> { 글제목[0] } <span onClick={ () => { likeUpdate( like + 1) } }>❤️</span> { like } </h3>
        <p>6월 25일 발행</p>
        <hr/>
      </div>
    </div>
  );
}

export default App;