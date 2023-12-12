import { useState } from 'react'
import Container from "react-bootstrap/Container"
import Row from "react-bootstrap/Row"
import Menu from "./components/Menu.jsx"
import { Outlet } from "react-router-dom"
import './App.css'
import RouterWithUserContext from './router.jsx'

function App() {
  return (
    <>
       <Menu />
        <Container>
          <Row style={{ textAlign: "center" }}>
          </Row>
          <Outlet/>
        </Container>
    </>
  )
}

export default App
