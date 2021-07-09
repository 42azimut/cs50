import { useEffect, useState } from "react"
import { Link } from "react-router-dom"

export default function DayList() {
  const [days, setDays] = useState([])

  useEffect(() => {
    fetch("http://localhost:3000/days")
      .then(res => {
        return res.json()
      })
      .then(data => {
        setDays(data)
      });
  }, []);   //count 가 변경되었을때만 실행 : 의존성 배열!!

  return (
      <ul className="list_day">
        {days.map(day => (
          <li key={day.id}>
            <Link to={`/day/${day.day}`}> Day { day.day } </Link>
          </li>
        ))}
      </ul> 
  );
}
