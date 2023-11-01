import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  let guesses = []
  const randomNumber = Math.floor(Math.random() * 50) + 1

  const takeAGuess = (e) => {
    e.preventDefault()
  }

  return (
    <>
      <h1>Guess the number</h1>
      <form onSubmit={(e)=>takeAGuess(e)}>

        <input type="number"/>
        <button type="submit">Submit</button>
      </form>
    </>
  )
}

export default App
