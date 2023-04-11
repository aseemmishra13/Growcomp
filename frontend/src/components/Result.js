import React from 'react'
import Res from './Res'

const Result = ({res}) => {
  return (
    res.map(r=>{
        return <Res key={r.id} r={r}/>
        }))
  
}

export default Result