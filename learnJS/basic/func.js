// normal function
function fun(){
    console.log('Hi')
}

fun()


// anonymous function

const resp = function (){
    console.log('success')
    return 'success'
}

let x = resp()
console.log(x)

// arrow function

const resp1 = () => 'success1'
let y = resp1()
console.log(y)

// arrow function - with multipls args

const resp2 = (arg1,arg2) => arg1+arg2
let z = resp2('hi ', 'there')
console.log(z)

// arrow function - with multipls args and multiple code block

const resp3 = (arg1,arg2) => {
    const arg3 = arg1+arg2
    return arg3

}
let z1 = resp3('hiii ', 'thereeeee')
console.log(z1)
