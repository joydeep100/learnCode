//for
for(let i=0;i < 10;i++){
    if(i===2) continue
    if(i===5) break
    console.log(i)
}

//while
let i=100
while(i < 110){
    console.log(i)
    i++
    if(i===105) break
}

//map
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(item => item * 2);
console.log(doubled); // [2, 4, 6, 8]

//filter
const numbers = [1, 2, 3, 4];
const evens = numbers.filter(item => item % 2 === 0);
console.log(evens); // [2, 4]