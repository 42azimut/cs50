import './App.css';


function App() {

  let posts = '스테이크 맛집'
  let post_style = { color: 'blue', fontSize: '30px' }

  function fn100() {
    return 100
  }
  return (
    <div className="App">
      <div className="black-nav">
        <div className={ posts }>blog study for React</div>
        <div style={ post_style }>style dev</div>
      </div>
        <h4> { posts } </h4>
        <h4> { fn100() } </h4>
    </div>
  );
}

export default App;
                           