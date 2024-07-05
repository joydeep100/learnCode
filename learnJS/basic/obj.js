const obj = {
    fname: 'joydeep',
    lname: 'das'
}

console.log(obj.fname)
console.log(obj['fname'])

//adding an element

obj.age = 10
console.log(obj)
// p.s. you can see that even when we decalare objs as const we are still able to mutate them
// this is because the reference address of the actual object is same but object content gets mutated and is legal

//deleting an element

delete obj.age
console.log(obj)

const obj2 = {
    fname: 'joydeep',
    lname: 'das',
    calcAge: age => 200 + age   //embedding a function inside an object
}

console.log(obj2.calcAge(10))
