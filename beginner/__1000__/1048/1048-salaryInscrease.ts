// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
//const input: string = `800.01`
const lines48: string[] = input.split('\n')

let salary: number = Number(lines48.shift())

const output = (arr: number[]): void => {

    let response: string[] = [
        `Novo salario: ${arr[0].toFixed(2)}`,
        `Reajuste ganho: ${arr[1].toFixed(2)}`,
        `Em percentual: ${arr[2]} %`
    ] 

    console.log(response.join('\n'))
}

const ReadJustment = (value: number, increase: number) => {
    const reajust = (value * increase) / 100;
    const newSalary = Number(value + reajust)

    output([newSalary, reajust, increase])
}
 
const Input = (salary: number): void => {

    if(salary >= 0 && salary <= 400){
        ReadJustment(salary, 15)

    } else if(salary >= 400.01 && salary <= 800){
        ReadJustment(salary, 12)

    }  else if(salary >= 800.01 && salary <= 1200){
        ReadJustment(salary, 10)

    }  else if(salary >= 1200.01 && salary <= 2000){
        ReadJustment(salary, 7)

    } else if (salary > 2000.01){
        ReadJustment(salary, 4)
    }
    
}

Input(salary)