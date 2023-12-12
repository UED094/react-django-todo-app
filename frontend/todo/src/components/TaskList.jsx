import React, { useEffect, useState } from "react";

const TaskList = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/todos/");
        const data = await response.json();
        setTasks(data);
      } catch (error) {
        console.log("Error fetching todos:", error);
      }
    };

    fetchData();
  }, []);

  return (
    <>
      <h1> Task List</h1>
      {tasks.map((task) => (
        <p key={task.id}> {task.description} </p>
      ))}
    </>
  );
};

export default TaskList;
