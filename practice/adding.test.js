// const { describe } = require("yargs")
const factorial = require("./factorial.js")

describe("Writing a simple factorial test", () => {
    test("Testing factorial to ensure it works properly", () => {
        expect(factorial(4)).toBe(24)
    })
})
test("Testing factorial to ensure it works properly", () => {
    expect(factorial(4)).not.toBe(23)
});

describe("tests factorial for large numbers", () => {
    test("tests factorial(10) = 3628800", () => {
        expect(factorial(10)).toBe(3628800);
    });

    test("tests factorial(20) = 2432902008176640000", () => {
        expect(factorial(20)).toBe(2432902008176640000);
    });
})
// describe("Checking a name function", () => {
//     test("makeAName function with two paramters", () => {
//         const makeAName
//     })
// })