import React,{useContext} from 'react'
import {Navbar, Nav, Container, NavDropdown} from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { Cartcontext } from '../context/Context'
const Header = () => {
  const {info,wres, setWRes,ares, setARes,hres, setHRes,tres, setTRes}= useContext(Cartcontext)
  const cartItems = info.state  
  const dispatch=info.dispatch
    let a = cartItems.length

  return (
    <header>
<Navbar bg="dark" variant='dark' expand="lg" collapseOnSelect>
      <Container >
      <LinkContainer to='/'>
        <Navbar.Brand >GrowComp</Navbar.Brand>
        </LinkContainer>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="ms-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <LinkContainer to='/cart'>
            <Nav.Link href="#action1"><i className='fas fa-shopping-cart'></i> Cart  {a===0?'':`(${a})`}</Nav.Link>
            </LinkContainer>
            <Nav.Link href="#action1"><i className='fas fa-user'></i> Sign In</Nav.Link>
            
         
            
           
          </Nav>
          
        </Navbar.Collapse>
      </Container>
    </Navbar>

    </header>
  )
}

export default Header