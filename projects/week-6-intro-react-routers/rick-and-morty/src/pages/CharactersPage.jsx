import axios from 'axios';
import {useEffect, useState} from 'react';
import Card from 'react-bootstrap/Card'
import GetCard from '../components/Card.jsx'

const CharactersPage = () => {
const url = "https://rickandmortyapi.com/api/character/?page="
const [characters, setCharacters] = useState([]);
const [page, setPage] = useState(1);

//name, status, species, image
const getCharactersByPage = async(pageNumber) => {
    console.log(pageNumber)
    let response = await axios.get(url + pageNumber)
    setCharacters([...characters, response.data.results])
    if (page < 42) { setPage(page + 1) }
    // console.log(characters)
  }

    useEffect (() => {
        getCharactersByPage(page)
    }, [page])

    useEffect (() => {
        console.log(characters)
    }, [characters])

    return (
        <>
        <h2>Characters</h2>
        <div className='my-card'>
            {characters.map((e, idx)=>(
            // key = {idx}
            <GetCard name= {e[1].name} 
            image={e[1].image}
            status={e[1].status}
            species={e[1].species}/>
            ))}
        </div>
        </>
    )
}

export default CharactersPage;

