import './App.css'
import { Outlet, Link } from 'react-router-dom'
// import NavBar from './components/NavBar.jsx'

function App() {
 
// only render homepage if I'm currently in localhost:5173/
  return (
    <>
      <img id="title" src ="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Rick_and_Morty.svg/800px-Rick_and_Morty.svg.png"/>
      {/* <NavBar/> */}
      <nav>
        <ul>
          <li><Link to='/'>Home</Link></li>
          <li><Link to='about/'>About</Link></li>
          <li><Link to='characters/'>Characters</Link></li>
        </ul>
      </nav>
      <Outlet />
    </>
  )
}

export default App
