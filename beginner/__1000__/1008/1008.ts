const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

let employee_number = Number(lines[0])
let worked_hours = Number(lines[1])
let received_hour = Number(lines[2])

let Salary = (worked_hours * received_hour)

let output: string[] = [
    `NUMBER = ${employee_number}`, 
    `SALARY = U$ ${Salary.toFixed(2)}`
]

output.forEach(line => console.log(line))