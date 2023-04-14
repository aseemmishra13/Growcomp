import React, { useContext } from 'react'
import { Button, Row,Col } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { Cartcontext } from '../context/Context'

const Cart = () => {
    const {info,wres, setWRes,ares, setARes,hres, setHRes,tres, setTRes}= useContext(Cartcontext)
    const cartItems = info.state  
    const dispatch=info.dispatch
   
    var total1=0
    var total2=0
    var total3=0
    var total4=0
  return (
    <div>
        <Link to='/'>
        <Button variant="primary" className=' my-1' >Go Back</Button></Link>
        
        <h3 className=' my-4'>
            Cart Items:
        </h3>
        {cartItems.length==0 && <div> No items added</div>}
        <div>
        <Row>
   <Col> <h3> Walmart</h3>
   
   { 
   cartItems.map((item)=>(
           item.company=='walmart' ?   (<div key={item.id}>


                    <h5>{item.title}</h5>
                    <h5>${item.price}</h5>
                <p hidden>    { total1= total1+item.price}</p>
                    
                    </div>):null
            ))}
          <h4> Total: ${total1}</h4>
   
   </Col>
   <Col> <h3> Amazon</h3>
   {cartItems.map((item)=>(
           item.company=='amazon' ?   (
           <div key={item.id}>


                    <h5>{item.title}</h5>
                    <h5>${item.price}</h5>
                    <p hidden>    { total2= total2+item.price}</p>
                    </div>):null
            ))}
   
   <h4> Total: ${total2}</h4>
   </Col>
   <Col> <h3> Harris Teeter</h3>
   {cartItems.map((item)=>(
           item.company=='harris' ?   (<div key={item.id}>


                    <h5>{item.title}</h5>
                    <h5>${item.price}</h5>
                    <p hidden>    { total3= total3+item.price}</p>
                    </div>):null
            ))}
   
   <h4> Total: ${total3}</h4>
   
   </Col>
   <Col> <h3> Target</h3>
   
   {cartItems.map((item)=>(
           item.company=='target' ?   (<div key={item.id}>


                    <h5>{item.title}</h5>
                    <h5>${item.price}</h5>
                    <p hidden>    { total4= total4+item.price}</p>
                    </div>):null
            ))}

<h4> Total: ${total4}</h4>
   
   </Col>
   </Row>
   <Button variant="primary" className=' my-1' onClick={()=>dispatch({type:'RESET',payload:{}})}>Reset</Button> 
        </div>


    </div>
  )
}

export default Cart