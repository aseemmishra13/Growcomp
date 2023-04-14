import { createContext, useReducer,useState } from "react";

export const Cartcontext= createContext()
export const Context=(props)=>{
    const reducer = (state,action)=>{
            switch(action.type){
                case 'ADD':
                    return [...state,action.payload]
                    case 'RESET':
                        return []    

                default: return state
            }
    }
    const [wres, setWRes]= useState([])
    const [ares, setARes]= useState([])
    const [hres, setHRes]= useState([])
    const [tres, setTRes]= useState([])
    const [state,dispatch] = useReducer(reducer,[]);
    const info={state,dispatch}
    return <Cartcontext.Provider value={{info,wres, setWRes,ares, setARes,hres, setHRes,tres, setTRes}}>{props.children}</Cartcontext.Provider>
}