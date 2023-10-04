const input = `5 3
Maria
João
Carlos
Vanessa
Jose`;

let lines = input.split('\n');

let [students, receiver ] = lines.shift().split(' ')
let sortedNames = lines.sort((a, b) => a.localeCompare(b))
let receiveName = sortedNames[+receiver - 1];

console.log(receiveName);