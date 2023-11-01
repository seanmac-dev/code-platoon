import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from "axios";


function App() {
  const getPokemon = async () => {
    
    try {
      
      for (let i = 1; i <= 6; i++) {
        const random = Math.floor(Math.random() * 1000) + 1
        const response = await axios.get("https://pokeapi.co/api/v2/pokemon/" + random);
        let pokemonPhoto = response.data.sprites.front_default;
        let img = document.getElementById("pokemonImg" + i)
        img.src = pokemonPhoto;
        }
    } catch (error) {
        console.log("Error:", error);
    }
  };

  return (
    <div style={{backgroundImage: `url(https://wallpapercave.com/wp/wp2878389.jpg)`}}>
    <>
    <main>
      <div class="background">
    <header>
      <img id="top-img" src= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdbGjmL2PerySmpM9_o24SwThuPRgLRirv0w&usqp=CAU" alt = "Pokemon Logo">
      </img>
    </header>
    <h1>Gotta Catch 'Em All!</h1>
      <div className="card">
        <button onClick={getPokemon}> 
          <img src={"https://cdn.pixabay.com/photo/2016/07/20/12/41/pokemon-1530315_1280.png"} className="logo" alt="Pokemon Ball logo" />
        </button>
    <h2>Create Your Team</h2>
      </div>
      <img src="" id="pokemonImg1" />
      <img src="" id="pokemonImg2" />
      <img src="" id="pokemonImg3" />
      <img src="" id="pokemonImg4" />
      <img src="" id="pokemonImg5" />
      <img src="" id="pokemonImg6" />
      </div>
      </main>
    </>
    </div>
  )
}

export default App
