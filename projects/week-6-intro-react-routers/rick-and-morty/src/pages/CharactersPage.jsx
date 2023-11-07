import axios from 'axios';
import {useEffect, useState} from 'react';
import GetCard from '../components/Card.jsx'
import { useOutletContext } from 'react-router-dom';

const CharactersPage = () => {

const url = "https://rickandmortyapi.com/api/character/?page="
const [characters, setCharacters] = useState([]);
const [page, setPage] = useState(1);
const { setFavorites, favorites } = useOutletContext();

//name, status, species, image
const getCharactersByPage = async(pageNumber) => {
    console.log(pageNumber)
    let response = await axios.get(url + pageNumber)
    setCharacters([...characters, response.data.results])
    console.log(setCharacters([...characters, response.data.results]))
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
            <GetCard 
            id={e[0].id}
            name= {e[0].name} 
            image={e[0].image}
            status={e[0].status}
            species={e[0].species}
            setFavorites={setFavorites}
            favorites={favorites}
            />
            ))}
        </div>
        </>
    )
}

export default CharactersPage;

