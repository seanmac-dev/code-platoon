import { useState } from 'react'
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Menu from "./components/Menu.jsx"
import { Outlet } from "react-router-dom"
import './App.css'
import { api } from "./utilities"

function App() {
  const token = localStorage.getItem("token");
  if (token) {
    api.defaults.headers.common["Authorization"] = `Token ${token}`
    console.log(`axios request authorization header set to: ${api.defaults.headers.common["Authorization"]}`);
  }
  return (
    <Container>
      <Row style={{ textAlign: "center" }}>
      </Row>
      <Menu />
      <Outlet/>
    </Container>
  )
}

export default App
