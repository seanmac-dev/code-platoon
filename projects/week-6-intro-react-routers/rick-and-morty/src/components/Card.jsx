import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';


function GetCard({name, image, species, status}) {
  return (
    
    <Card className='i-card'style={{ width: '18rem' }} >
      <Card.Img variant="top" src={image} />
      <Card.Body>
        <Card.Title>{name}</Card.Title>
        <Card.Text>
        
        Species: {species}
        <br></br>Status: {status}
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card>
  );
}

export default GetCard;