import { Link } from 'react-router-dom'

const NavBar = ({favorites}) => {
    return (
        <nav>
            <ul>
                <li><Link to='/'>Home</Link></li>
                <li><Link to='about/'>About</Link></li>
                <li><Link to='characters/'>All Characters</Link></li>
                <li><Link to='favorites/'>Favorites {favorites.length}</Link></li>
            </ul>
        </nav>

    )
}

export default NavBar;