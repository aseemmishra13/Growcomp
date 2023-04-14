import React ,{useState}from 'react';
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom'
import {Container} from 'react-bootstrap';
import Footer from './components/Footer';
import Header from './components/Header';
import Search from './components/Search';
import Cart from './components/Cart';

import Res from './components/Res';
import Result from './components/Result';
const App=()=> {
  const [cartItems,setCartItems]=useState([])
  const handleAddProduct = (r)=>{
    
    setCartItems([...cartItems,{...r}])
    console.log(cartItems)
    
  }
 
  return (
    <Router>
    <div className="App">
      <Header cartItems={cartItems}/>
      <main className='py-3'>
      <Container>
     
      
      <div className='px-2 '>
        
        <Routes>
        <Route path ='/' element={<Search cartItems={cartItems} />} exact/>
        <Route path ='/search' element={<Result />} exact/>
        <Route path ='/cart/' element={<Cart  cartItems={cartItems}/>}/>
      
      </Routes>
      </div>
      </Container>
      </main>
      <Footer />
    </div>
    </Router>
  );
}

export default App;
