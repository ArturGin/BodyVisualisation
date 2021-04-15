import React from 'react'
import Task from './Task'

export const Tasks = ({ tasks, onDelete, onChoosen }) => {
    return (
        <div>
            {tasks.map((task) => (
                <Task key={task.id} 
                task={task} 
                onDelete={onDelete}
                onChoosen={onChoosen}>

                </Task>
            ))}
        </div>
    )
}


export default Tasks