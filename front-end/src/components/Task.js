// Love React already. The system built upon modulation
// and reducing everything to the last bit

import React from 'react'
import { FaTimes } from 'react-icons/fa'

export const Task = ({ task, onDelete, onChoosen }) => {
    return (
        <div className='task' 
        onDoubleClick={() => onChoosen(task.id)}>
            <h3>
                {task.text} 
                <FaTimes 
                style={{ cursor: 'pointer'}}
                // fucky syntax but that how we pass a var to func in App.js
                onClick={() => {onDelete(task.id)}}
                >

                </FaTimes>
            </h3>
            
        </div>
    )
}

export default Task