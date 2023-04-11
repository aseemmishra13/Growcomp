import React from 'react';
import {Container} from 'react-bootstrap';
import Footer from './components/Footer';
import Header from './components/Header';
import Search from './components/Search';


const App=()=> {
  return (
    <div className="App">
      <Header />
      <main className='py-3'>
      <Container>

      <h1>Welcome To GrowComp</h1>
      <div className='px-2 py-5'>
        <h3> Start Searching</h3>
      <Search />
      </div>
      </Container>
      </main>
      <Footer />
    </div>
  );
}

export default App;
