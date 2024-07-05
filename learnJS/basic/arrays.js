// arrays

const a = [1,2,'3']
console.log(a[2])

// or

const b = new Array(1,2,'3')
console.log(b[2])

// aarays operations
console.log(b.length)

console.log(1 in b)
console.log('1' in b)
// true
// true

//notice that if we use in operator it checks for == , but when we used includes keyword it checks for ====
//hence in keyword should never be used as a thumb rule
console.log(b.includes(1))
console.log(b.includes('1'))
// true
// false

// add / remove at the end
const c = [1,2,3,4]
c.push(5)
console.log(c)
//[1,2,3,4,5]
c.pop()
console.log(c)
//[1,2,3,4]

// add / remove at the beginning
const d = [2,3,4]
d.unshift(1)
console.log(d)
// [ 1, 2, 3, 4 ]
d.shift()
console.log(d)
// [ 2, 3, 4 ]

