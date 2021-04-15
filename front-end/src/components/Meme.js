import React from 'react'

const Meme = (props) => {
    return (
        <div>
          <h1>{props.title}</h1>
          <h2>{props.someName}</h2>
        </div>
    )
}

Meme.defaultProps = {
    title: 'Bruh1',
    someName: 'bruh1',
  }

// also we can do defualt types and is the field requirerd

// style can be written directly in JS
export default Meme
