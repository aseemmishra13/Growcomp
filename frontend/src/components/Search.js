import React,{useState,useRef, useContext} from 'react'
import{Button, Form} from 'react-bootstrap'
import { Cartcontext } from '../context/Context'
import Result from './Result'
import Res from './Res'
import { Row ,Col} from 'react-bootstrap'
const Search = () => {
  const {info,wres, setWRes,ares, setARes,hres, setHRes,tres, setTRes}= useContext(Cartcontext)
    const cartItems = info.state  
    const dispatch=info.dispatch
  const [bool, setBool]= useState([])


 
    const searchref= useRef()

    const getSearch=async(search)=>{

     let a = await fetch(`http://127.0.0.1:8000/result/walmart/${search}/`)
     let data= await a.json()
     
     
     

     let b = await fetch(`http://127.0.0.1:8000/result/amazon/${search}/`)
     let data1= await b.json()
     console.log(data1)

     let d = await fetch(`http://127.0.0.1:8000/result/target/${search}/`)
     let data3= await d.json()
     setWRes(data)
     setARes(data1)
     
     setTRes(data3)
     

     let c = await fetch(`http://127.0.0.1:8000/result/harris/${search}/`)
     let data2= await c.json()
    
     
     setHRes(data2)
   
      

    }
    
    const handleClicl=(e)=>{
        const search=searchref.current.value
       getSearch(search)
        
        
        

    }


  return (
    <div  >
        <h1>Welcome To GrowComp</h1>

        <h3 className='px-2 py-5'> Start Searching</h3>
        <Form  className='py-3 text-center'>
        <Form.Group className="mb-3 " controlId="formBasicEmail">
      
        <Form.Control ref={searchref}  type="text" placeholder="Start typing" className='py-3' />
        
     
      
      </Form.Group>
      <Button className='btn-circle btn-xl' variant="primary" type="button" onClick={handleClicl}  >
        Search
      </Button>

        </Form>
        <Row>
   <Col> <h3> Walmart</h3>
   { Array.from(wres).map(r=>(
    
     
    <Col >
    
    <Res key = {r.id} r={r} cartItems={cartItems} />
    </Col>
    ))}
   
   </Col>
   <Col> <h3> Amazon</h3>
   { Array.from(ares).map(r=>(
         <Col >
       <Res key = {r.id} r={r}cartItems={cartItems} />
       </Col>
       ))}
   
   </Col>
   <Col> <h3>Harris Teeter</h3>
   { Array.from(hres).map(r=>(
         <Col >
       <Res key = {r.id} r={r} cartItems={cartItems} />
       </Col>
       ))}
   </Col>
   <Col> <h3> Target</h3>
   
   { Array.from(tres).map(r=>(
    
     
    <Col >
    
    <Res key = {r.id} r={r} cartItems={cartItems} />
    </Col>
    ))}
   
   </Col>
 </Row>




    </div>
  )
}

export default Search