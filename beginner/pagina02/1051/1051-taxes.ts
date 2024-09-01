// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
//const input: string = `20.00`
const lines51 = input.split('\n').map((item: string) => Number(item));

let Salary = Number(lines51.shift())

const Taxe = (salary: number) => {

    let taxe = 0
    if(salary > 2000 && salary <= 3000){
        taxe = 2
    }
    
    if(salary > 3000 && salary <= 4500){
        taxe = 3
    }
    
    if(salary > 4500) {
        taxe = 4
    }

    return taxe
}

const Main = (salary: number): void => {

    const taxAbove2000 = (salary - 2000) * 0.08;
    const taxAbove3000 = (salary - 3000) * 0.18 + 80;
    const taxAbove4500 = (salary - 4500) * 0.28 + 350; 

    let taxe = Taxe(salary)


    if(taxe === 2){
        console.log(`R$ ${taxAbove2000.toFixed(2)}`)

    } else if(taxe === 3){
        console.log(`R$ ${taxAbove3000.toFixed(2)}`) 

    } else if(taxe === 4){
        console.log(`R$ ${taxAbove4500.toFixed(2)}`) 

    } else {
        console.log("Isento")
    }
}

Main(Salary)