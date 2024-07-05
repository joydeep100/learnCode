'use strict';

function logger(){
    console.log('I am logger function')
}

const anonymousLogger = function (){
    console.log('I am anonumous funtion')
}

const arrowLogger = () => console.log('I am an arrow function');

logger()
logger()

anonymousLogger()
arrowLogger()

// let hasDL = false;
// const passTest = true;

// objects
const obj1 = {
    a: 1,
    bFun: function(arg1){
        return `bFun ${this.a} ${arg1}`
    }
}

// how to embed a function inside of an object and also how to use some of the object
// properties

console.log(obj1.bFun('Nice'))

