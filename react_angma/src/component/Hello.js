import { useState } from "react";
import UserName from "./UserName";

export default  function Hello({age}) {
  // let name = "Jayden"
  const [name, setName] = useState("Jayden");
  const msg = age > 19 ? "성인 입니다." : "미성년자 입니다."
  //const [age, setAge] = useState(props.age)
  
  function changName() {
    const newName = name === "Jayden" ? "Mike" : "Jayden"
    //document.getElementById("name").innerText = name;
    setName(newName)
  }

  return (
    <div>
      <h2 id="name">{name}({age}) : {msg}</h2>
      <UserName name={name} />
      <button onClick={changName}>Change</button>
    </div>
    )
}
