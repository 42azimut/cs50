import { useParams } from "react-router";
import Word from "./Word"
import { useEffect, useState } from "react"

export default function Day() {
  // dummy.words
  const { day } = useParams();
  // const wordList = dummy.words.filter(word => word.day === Number(day));
  const [words, setWords] = useState([])

  useEffect(() => {
    fetch("http://localhost:3000/words")
      .then(res => {
        return res.json()
      })
      .then(data => {
        setWords(data)
      });
  }, []); 
  
  return (
    <>
    <h2>Day {day}</h2>
      <table>
        <tbody>
          {words.map(word => (
          <Word word={word} key={word.id} />
          ))}
        </tbody>
      </table>
    </>
  );
}
