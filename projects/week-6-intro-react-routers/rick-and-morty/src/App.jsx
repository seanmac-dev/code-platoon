import './App.css'
import { Outlet } from 'react-router-dom'
import { useEffect, useState } from 'react'
import NavBar from './components/NavBar.jsx'

function App() {
  const [favorites, setFavorites] = useState([])

  useEffect(()=> {
    console.log(favorites)
  }, [favorites])
 
// only render homepage if I'm currently in localhost:5173/
  return (
    <>
      <img id="title" src ="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Rick_and_Morty.svg/800px-Rick_and_Morty.svg.png"/>
     
      <NavBar favorites={favorites}/>
      <Outlet context={{favorites, setFavorites}}/>
    </>
  )
}

export default App
