import { useState } from "react";

export default  function Hello() {
  // let name = "Jayden"
  const [name, setName] = useState("Jayden");
  
  function changName() {
    const newName = name === "Jayden" ? "Mike" : "Jayden"
    //document.getElementById("name").innerText = name;
    setName(newName)
  }

  return (
    <div>
      <h1>state</h1>
      <h2 id="name">{name} </h2>
      <button onClick={changName}>Change</button>
    </div>
    )
}
