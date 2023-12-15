import Row from "react-bootstrap/Row"
import { useEffect, useState } from "react";
// import { api } from "../utilities";

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
  const [cryptoDataList, setCryptoDataList] = useState([]);
  const [cryptoName, setCryptoName] = useState([])
 

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
      setCryptoDataList((prevCryptoDataList) => {
        // Find the index of the cryptocurrency data in the list
        const index = prevCryptoDataList.findIndex(
          (cryptoData) => cryptoData.FROMSYMBOL === data.data.FROMSYMBOL
        );
      
        if (index !== -1) {
          // If the cryptocurrency data exists in the list, update it
          prevCryptoDataList[index] = data.data;
          return [...prevCryptoDataList]; // Create a new array to trigger a re-render
        } else {
          // If the cryptocurrency data doesn't exist, add it to the list
          return [...prevCryptoDataList, data.data];
        }
      });

    socket.addEventListener('close', (event) => {
      console.log('WebSocket closed:', event);
    });

    // Clean up the WebSocket connection when the component unmounts
    return () => {
      socket.close();
    };
  })
  }, []);

  const subscribeToChannels = (socket) => {
    const subscriptions = [
      "5~CCCAGG~BTC~USD", "5~CCCAGG~ETH~USD","5~CCCAGG~XRP~USD" 
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
      {cryptoDataList && cryptoDataList.map((cryptoData) => (
        <div key={cryptoData.FROMSYMBOL}>
          <h3>{cryptoData.FROMSYMBOL}</h3>
          <li>
            Price: {cryptoData.PRICE}
            <br />
            Daily Volume (last 24 hours): {cryptoData.VOLUME24HOUR}
            <br />
            Market Cap: {cryptoData.CURRENTSUPPLYMKTCAP}
            <br />
          </li>
        </div>
      ))}
    </ul>
  </Row>
  );
}