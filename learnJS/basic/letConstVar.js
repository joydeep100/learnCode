// const - use const to declare all variables by default which do not change

const a = 1

// note that uninitialized const declarations are illegal, i.e. const a

// let - use let when you are sure the variable is going to change in future
let age = 10
age = 11

/*
however this is not allowed
let age = 10
let age = 11
 */

// avoid var, this is legacy way of declaring variables before ES6
var a = 10
var a = 20
// this works here, hence not recommended

