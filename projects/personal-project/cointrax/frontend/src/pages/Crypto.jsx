import Row from "react-bootstrap/Row"
import { useEffect, useState } from "react";
import { api } from "../utilities";

// TODO: make axios call to django api to get crypto data
// using api/v1/crypto

export const Crypto = () => {
    const [crypto, setCrypto] = useState([]);

    const getAllCrypto = async () => {
        console.log('getAllCrypto works'); 
        try {
            let response = await api.get("v1/crypto/");
            console.log(response.data);
            setCrypto(response.data);
        } catch (error) {                    
        console.log('getAllCrypto err ', error);
        }
    }
    useEffect(() => {
        getAllCrypto();
    }, [])

    return (
        <Row style={{ padding: "0 10vmin" }}>
          <h1 style={{ textAlign: "center" }}>Crypto</h1>
          <ul>
            {crypto.map((c) => (
              <li key={c.id}>
                Name: {c.name}
                <br />
                Symbol: {c.symbol}
                <br />
                Price: {c.price}
                <br />
                Circulating Supply: {c.circulating_supply}
                {/* <ul>
                  Pokemon
                  {move.pokemon.map((poke) => (
                    <li>{poke}</li>
                  ))}
                </ul> */}
              </li>
            ))}
          </ul>
        </Row>
      );
    };