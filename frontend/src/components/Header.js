import React from 'react'
import {Navbar, Nav, Container, NavDropdown} from 'react-bootstrap'
const Header = () => {
  return (
    <header>
<Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
      <Container >
        <Navbar.Brand href="#">GrowComp</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="ms-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link href="#action1"><i className='fas fa-shopping-cart'></i> Cart</Nav.Link>
            <Nav.Link href="#action1"><i className='fas fa-user'></i> Sign In</Nav.Link>
            
         
            
           
          </Nav>
          
        </Navbar.Collapse>
      </Container>
    </Navbar>

    </header>
  )
}

export default Header