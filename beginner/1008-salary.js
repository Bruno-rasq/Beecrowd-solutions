let employee_number = Number(lines[0]);
let worked_hours = Number(lines[1]);
let received_hour = Number(lines[2]);

let Salary = (worked_hours * received_hour);
console.log(`NUMBER = ${employee_number}`);
console.log(`SALARY = U$ ${Salary.toFixed(2)}`);