import React, { useState, useEffect } from 'react'
import './illustrations.scss'
import P5Wrapper from 'react-p5-wrapper';
import sketch from "./sketch.js"
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/disasters/list/';

export const Illustration = (p) => {
    

     return (
        <P5Wrapper sketch={sketch}/>
    )
};



export default Illustration


// Todo

//1. Text in a circle from the API around the figure
//1.1 Get camera to spin around

//2. Representation/An actual figure