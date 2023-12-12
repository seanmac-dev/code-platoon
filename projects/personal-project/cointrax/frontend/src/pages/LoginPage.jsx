// LoginPage.jsx
import { useState } from "react";
import { api } from "../utilities.jsx";
import { useNavigate } from "react-router-dom";
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';


export const Login = () => {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Assuming userName and password are state variables or retrieved from the form
      let response = await api.post("v1/users/login/", {
        email,
        password,
      });

      let userEmail = response.data.email;
      console.log(userEmail)
      let token = response.data.token;
      console.log(token)

      // Store the token securely (e.g., in localStorage or HttpOnly cookies)
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Token ${token}`;

      // Update the user context
      // setUser(user);

      // Redirect to the desired page after successful login
      navigate("/crypto");
    } catch (error) {
      console.error("Login failed:", error.message);
    }
  };

  return (
    <Form onSubmit={handleLogin}>
      <Form.Group className="mb-3" controlId="formBasicEmail">
        <Form.Label>Email address</Form.Label>
        <Form.Control
          type="email"
          placeholder="Enter email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <Form.Text className="text-muted">
          We'll never share your email with anyone else.
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

      {/* <Form.Group className="mb-3" controlId="formBasicCheckbox">
        <Form.Check type="checkbox" label="Check me out" />
      </Form.Group> */}

      <Button variant="primary" type="submit">
        Login
      </Button>
    </Form>
  );
};

export default Login;


