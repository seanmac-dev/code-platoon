import Row from "react-bootstrap/Row"
import { useEffect, useState } from "react";
import { api } from "../utilities";

// TODO: make axios call to django api to get crypto data
// using api/v1/crypto

// export const Crypto = () => {
//     const [crypto, setCrypto] = useState([]);

//     const getAllCrypto = async () => {
//         console.log('getAllCrypto works'); 
//         try {
//             let response = await api.get("v1/crypto/");
//             console.log(response.data);
//             setCrypto(response.data);
//         } catch (error) {                    
//         console.log('getAllCrypto err ', error);
//         }
//     }
//     useEffect(() => {
//         getAllCrypto();
//     }, [])
export const Crypto = () => {
  const [cryptoData, setCryptoData] = useState([]);

  useEffect(() => {
   
    const wsUrl = `ws://127.0.0.1:8000/ws/crypto/`;

    const socket = new WebSocket(wsUrl);

    socket.addEventListener('open', (event) => {
      console.log('WebSocket connected:', event);
      // Subscribe to channels after WebSocket is open
      subscribeToChannels(socket);
    });

    socket.addEventListener('message', (event) => {
      // Handle incoming data from the WebSocket
      const data = JSON.parse(event.data);
      console.log('Received data:', data);

      // Update your component state with the received data
      setCryptoData((prevData) => [...prevData, data]);
    });

    socket.addEventListener('close', (event) => {
      console.log('WebSocket closed:', event);
    });

    // Clean up the WebSocket connection when the component unmounts
    return () => {
      socket.close();
    };
  }, []);

  const subscribeToChannels = (socket) => {
    const subscriptions = [
      '5~CCCAGG~BTC~USD',
      '0~Coinbase~ETH~USD',
      '2~Binance~BTC~USDT',
    ];

    const subscribeMessage = {
      action: 'SubAdd',
      subs: subscriptions,
    };

    // Send the subscription message to the WebSocket
    socket.send(JSON.stringify(subscribeMessage));
  };

    return (
        <Row style={{ padding: "0 10vmin" }}>
          <h1 style={{ textAlign: "center" }}>Crypto</h1>
          <ul>
            {cryptoData.map((c, index) => (
              <li key={index}>
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