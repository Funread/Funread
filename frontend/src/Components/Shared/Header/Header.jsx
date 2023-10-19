import React from "react";
// import { Navbar, Nav } from "react-bootstrap";
import logoFunread from "../../../logoFunread.png";
import "./Header.sass";

import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import Offcanvas from 'react-bootstrap/Offcanvas';

class Header extends React.Component {
  render() {
    return (
      //Return Here component or html code
      <div className="header-navbar-container">
        <Navbar key='md' expand='md' className="bg-body-tertiary mb-3" bg="transparent" variant="dark">
          <Container fluid>
            <Navbar.Brand>
              <img
                src={logoFunread}
                alt="logo"
                className="header-navbar-logo-funread"
              ></img>
            </Navbar.Brand>
            <Navbar.Toggle aria-controls={`offcanvasNavbar-expand-md`} />
            <Navbar.Offcanvas id={`offcanvasNavbar-expand-md`} className='loading-page-header' aria-labelledby={`offcanvasNavbarLabel-expand-md`} placement="end">
              <Offcanvas.Header closeButton>
                <Offcanvas.Title id={`offcanvasNavbarLabel-expand-md`}>
                  Opciones {/* Quizas se deba escojer un mejor nombre para el menu o quitarle el titulo */}
                </Offcanvas.Title>
              </Offcanvas.Header>
              <Offcanvas.Body>
                <Nav className="justify-content-end flex-grow-1 pe-3">
                  <Nav.Link href="#action1">About Us</Nav.Link>
                  <Nav.Link href="#action2">Study Programs</Nav.Link>
                  <Nav.Link href="#action3">Recent Reports</Nav.Link>
                </Nav>
              </Offcanvas.Body>
            </Navbar.Offcanvas>
          </Container>
        </Navbar>
      </div>
    );
  }
}

export default Header;