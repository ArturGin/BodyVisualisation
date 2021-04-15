import React from 'react'
import Button from './Button'

const Header = (props) => {
    const onClick = () => {
        console.log('Fucking annoiyng')
    }
    return (
        <div className='header'>
            <h1>{props.title}</h1>
            <Button color='green'
             text = 'BruhLowder'
             onClick={onClick}
             >

             </Button>
        </div>
            
        
    )
}


Header.defaultProps = {
    title: 'Bruh1',
    button: 'Lowder!',
  }

export default Header

