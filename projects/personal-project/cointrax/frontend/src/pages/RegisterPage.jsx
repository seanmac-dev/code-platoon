import { useState } from "react";
import { useNavigate } from "react-router";
import { api } from "../utilities.jsx";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';



export const Register = () => {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [display_name, setDisplayName] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      console.log("Request Payload:", {
        email,
        password,
        display_name,
      });

      const response = await api.post("v1/users/signup/", {
        email,
        password,
        display_name,
      });

      let new_user = response.data.new_user;
      console.log(new_user)
      let token = response.data.token;
      console.log(token)
      console.log(`signup success, userEmail: ${email}, token: ${token}`)
      // Store the token securely (e.g., in localStorage or HttpOnly cookies)
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Token ${token}`;

      navigate("/login");
    } catch (error) {
      console.error("Registration failed:", error.message);
    }
  };

  return (
    <Form onSubmit={handleRegister}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <Form.Text className="text-muted">
          We'll never share your email with anyone.
        </Form.Text>
      </Form.Group>

      <Form.Group className="mb-3" controlId="formBasicPassword">
        <Form.Label>Password</Form.Label>
        <Form.Control
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </Form.Group>

      <Form.Group className="mb-3" controlId="formDisplayName">
        <Form.Label>Display Name</Form.Label>
        <Form.Control
          type="username"
          placeholder="hodler4days"
          value={display_name}
          onChange={(e) => setDisplayName(e.target.value)}
        />
      </Form.Group>

      {/* <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group> */}

      <Button variant="primary" type="submit">
        Submit
      </Button>
    </Form>
  );
};
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [displayName, setDisplayName] = useState("");

//   const signUp = async (e) => {
//     e.preventDefault();

//     try {
//       let response = await api.post("/v1/users/signup/", {
//         email: email,
//         password: password,
//         displayName: displayName,
//       });

//       let token = response.data.token;

//       // Store the token securely (e.g., in localStorage or HttpOnly cookies)
//       localStorage.setItem("token", token);
//       api.defaults.headers.common["Authorization"] = `Token ${token}`;

//       // Redirect or navigate to the home page
//       // Assuming you have a navigate function from a router library
//       // navigate("/home");

//       console.log("User registered successfully");
//     } catch (error) {
//       console.error("Registration failed:", error.message);
//     }
//   };

//   return (
//     <Form onSubmit={signUp}>
//       <Form.Group className="mb-3" controlId="formBasicEmail">
//         <Form.Label>Email address</Form.Label>
//         <Form.Control
//           type="email"
//           placeholder="Enter email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//         />
//         <Form.Text className="text-muted">
//           We'll never share your email with anyone else.
//         </Form.Text>
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Password</Form.Label>
//         <Form.Control
//           type="password"
//           placeholder="Password"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//         />
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicPassword">
//         <Form.Label>Display Name</Form.Label>
//         <Form.Control
//           type="displayName"
//           placeholder="hodler73"
//           value={displayName}
//           onChange={(e) => setDisplayName(e.target.value)}
//         />
//       </Form.Group>

//       <Form.Group className="mb-3" controlId="formBasicCheckbox">
//         <Form.Check type="checkbox" label="Check me out" />
//       </Form.Group>

//       <Button variant="primary" type="submit">
//         Submit
//       </Button>
//     </Form>
//   );
// }

