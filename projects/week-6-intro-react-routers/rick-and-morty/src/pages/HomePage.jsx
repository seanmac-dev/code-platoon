import { Link } from 'react-router-dom';

const HomePage = () => {

    return (
        <>
        <h1 id="enter-portal">Click the portal to get schwifty!</h1>
        <div className="portal-img-div">
        <Link to= 'characters/'>
        <img id="portal-img" src="https://png2.cleanpng.com/sh/b53629d3baa712f0f50c28962901fc23/L0KzQYm3VMA1N6Fuj5H0aYP2gLBuTgBweqVmhJ92b4L3iX76jfl1cF53gdV0LYPkfrTvhgoufF54gNt7dD3rf7FrifUueJD3jNN1LUXkc4XpUPNjbWNnetYALkS8SIW9VcQxOWY3Sqo8OUe4RYq5WMcveJ9s/kisspng-portal-morty-smith-rick-sanchez-t-shirt-hoodie-portal-5ac4b0cbe2bbd5.4984654015228397559287.png"/>
        </Link>
        </div>
        </>
    )
}

export default HomePage;