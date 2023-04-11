import React,{useState,useRef} from 'react'
import{Button, Form} from 'react-bootstrap'
import Result from './Result'
const Search = () => {
  const [res, setRes]= useState([{id:2,name:"PS5"}])
    const searchref= useRef()
    
    const handleClicl=(e)=>{
        const search=searchref.current.value
        console.log(search)
        setRes(prevres =>{
            return[...prevres,{id:1,name:search}]

        })

    }


  return (
    <div  >

        <Form  className='py-3 text-center'>
        <Form.Group className="mb-3 " controlId="formBasicEmail">
      
        <Form.Control ref={searchref}  type="email" placeholder="Start typing" className='py-3' />
        
     
      
      </Form.Group>
      <Button className='btn-circle btn-xl' variant="primary" type="button" onClick={handleClicl}  >
        Search
      </Button>

        </Form>
        <Result res={res}/>




    </div>
  )
}

export default Search