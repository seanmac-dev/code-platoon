import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { useNavigate } from 'react-router-dom';



function GetCard({ id, name, image, species, status, setFavorites, favorites }) {
    
    const navigate = useNavigate()

    const shouldRoute=(id) => {
        navigate(`/character/${id}`);
    };

  return (
    
    <Card className='i-card'style={{ width: '18rem' }} >
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Card.Text>
        Species: {species}
        <br></br>
        Status: {status}
        </Card.Text>
        <Button 
            variant="primary" 
            onClick={()=> shouldRoute(id)}>
        Details
        </Button>
        <Button 
            variant="warning" 
            onClick={()=> setFavorites([
                console.log("inside favorites"),
                // ...(Array.isArray(favorites) ? favorites : []),
                ...favorites, {'id': id, 'name': name, 'image': image}
              ])}>
        Favorite
        </Button>
      </Card.Body>
    </Card>
  );
}

export default GetCard;