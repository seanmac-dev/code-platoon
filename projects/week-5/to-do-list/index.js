import axios from "axios";

const getPokemon = async () => {
    try {
        const response = await axios.get("https://pokeapi.co/api/v2/pokemon/ditto");
        console.log(response.data.sprites.front_default);
    } catch (error) {
        console.error("An error occurred:", error);
    }
};

getPokemon();





// import tasks from './tasks.json' assert {type: "json"};
// console.log(tasks);;

// // --MAPPING-- //
// // const { id, task, completed } = tasks[0];
// // console.log(`Task ${id}: ${task}, Completed: ${completed}`);

// // tasks.map(({ id, task, completed } = item) => {
// //     console.log(id, task, completed)
// // })

// // --FILTER-- //
// const completedTasks = tasks.filter((task) => {
//     return task.completed === true;
// });

// const incompleteTasks = tasks.filter((task) => {
//     return !task.completed;
// });

// console.log(tasks)
// console.log(completedTasks);
// console.log(incompleteTasks);