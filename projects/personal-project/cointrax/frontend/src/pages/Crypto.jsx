import Row from "react-bootstrap/Row"
import { useEffect } from "react";
import axios from "axios";

// TODO: make axios call to django api to get crypto data
// using api/v1/crypto

export const Crypto = () => {
    const getAllCrypto = async () => {
        console.log('getAllCrypto'); 
        let response = await axios
            .get("http://127.0.0.1:8000/api/v1/crypto/")   
            .catch((err) => {                    
                console.log('getAllCrypto err ', err);
                // alert("getAllCrypto err");
            })
    }

    useEffect(() => {
        getAllCrypto();
    }, [])

    return (
        <Row>
            <h1>Crypto</h1>
        </Row>
    );
}