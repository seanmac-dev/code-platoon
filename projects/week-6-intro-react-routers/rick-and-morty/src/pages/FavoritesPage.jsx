import { useOutletContext } from "react-router-dom";
import Card from "../components/Card";

const FavoritesPage = () => {
    const {setFavorites, favorites} = useOutletContext()

    return (
        <>
        <h2>Favorites</h2>
        {favorites.map((char)=>(
            <Card 
            id={char.id}
            name={char.name}
            image={char.image}
            setFavorites={setFavorites}
            favorites={favorites}
            />
        ))}
        </>
    );
};

export default FavoritesPage;