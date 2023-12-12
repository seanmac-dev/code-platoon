// LoginPage.jsx
import { api } from "../utilities.jsx";
import { useNavigate } from "react-router-dom";
import { useContext } from "react";
import UserContext from "../components/UserContext.js";

export const Login = () => {
  const navigate = useNavigate();
  const { setUser } = useContext(UserContext);

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      // Assuming userName and password are state variables or retrieved from the form
      let response = await api.post("v1/users/login/", {
        email: userName,
        password: password,
      });

      let token = response.data.token;
      let user = response.data.user;

      // Store the token securely (e.g., in localStorage or HttpOnly cookies)
      localStorage.setItem("token", token);
      api.defaults.headers.common["Authorization"] = `Token ${token}`;

      // Update the user context
      setUser(user);

      // Redirect to the desired page after successful login
      navigate("/crypto");
    } catch (error) {
      console.error("Login failed:", error.message);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      {/* Your login form content */}
      <button type="submit">Login</button>
    </form>
  );
};

export default Login;


