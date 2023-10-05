// const database = {
//     person1: {
//         name: "Sally",
//         age: 43
//     },
//     person2: {
//         name: "John",
//         age: 35
//     }
// }
// console.log(Object.values(database))
// console.log(Object.keys(database))
// console.log(Object.keys(database.person1))
// console.log(Object.values(database.person1))

// let myObj = {
//     "I": 1,
//     "II": 2,
//     "III": 3
// }
// // for (numeral in myObj) {
// //     console.log(numeral)
// // }
// // for (let item of Object.entries(myObj)) {
// //     console.log(item)
// // }
// for ([key, value] of Object.entries(myObj)) {
//     console.log(key)
//     console.log(value)
// }

// let myString = 'liksoniono'
// let letters = {}
// for (ltr of myString) {
//     if (letters[ltr]) {
//         letters[ltr] += 1
//     } else {
//         letters[ltr] = 1
//     }
// }
// console.log(letters)

// let myArray = [
//     1, 2, 3, 4, 5, 6
// ];

// myArray.map((placer, idx) => {
//     if (idx % 2 === 0) {
//         console.log(placer)
//     } else {
//         console.log(placer * 2)
//     }
// })
// // if index is divisible by 2, return that number. otherwise multiply it by 2
// // multiplies only even numbers by 2
// // 

// let [a, b, c, d, e] = ['a', 'b', 'c', 'd', 'e']
// console.log(e)

function factorial(num) {
    let product = 1;

    for (let i = num; i > 0; i--) {
        product = product * i;
    }

    return product;
}

module.exports = factorial;