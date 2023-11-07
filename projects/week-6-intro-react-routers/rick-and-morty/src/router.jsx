import { createBrowserRouter } from "react-router-dom";
import App from "./App"
import HomePage from './pages/HomePage.jsx'
import AboutPage from './pages/AboutPage.jsx'
import CharactersPage from './pages/CharactersPage.jsx'
import CharacterDetailsPage from './pages/CharacterDetailsPage'
import NotFoundPage from './pages/NotFoundPage.jsx'
import FavoritesPage from "./pages/FavoritesPage";

const router = createBrowserRouter([
    {
        // http://localhost:5173/
        path: "/",
        element: <App/>,
        children: [
            {
            index: true,
            element: <HomePage/>
            },
            {
                path: 'about/',
                element: <AboutPage />
            },
            {
                path: 'characters/',
                element: <CharactersPage />
            },
            {
                path: 'character/:id/',
                element: <CharacterDetailsPage />
            },
            {
                path: 'favorites/',
                element: <FavoritesPage />
            }
        ],
        errorElement: <NotFoundPage />
    }
])

export default router;