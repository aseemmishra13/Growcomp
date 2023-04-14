import React,{useState,useContext} from 'react'
import { Button,Row ,Card} from 'react-bootstrap'
import { Cartcontext } from '../context/Context'

const Res = ({r}) => {
 
  const {info,wres, setWRes,ares, setARes,hres, setHRes,tres, setTRes}= useContext(Cartcontext)
  const cartItems = info.state  
  const dispatch=info.dispatch
  console.log(info)
  return (
    <Card className="mb-2" style={{ width: '18rem' }}>
    <Card.Img variant="top" src={r.image} style={{ width: '18rem' ,height:'15rem'}} />
    <Card.Body>
      <Card.Title>{r.title}</Card.Title>
      <Card.Text>
      $ {r.price}
      </Card.Text>
      <Button variant="primary" onClick={()=>dispatch({type:'ADD',payload:r})} >Add to Cart</Button>
    </Card.Body>
  </Card>
  )
}

export default Res