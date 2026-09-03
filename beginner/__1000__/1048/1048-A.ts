import * as fs from "fs"
const salary: number = Number(fs.readFileSync("/dev/stdin", "utf8"))

const table_salary_readjustment_rate: number[][] = [
    //ini        #end            #% 
    [0,         400.00,         15],
    [400.01,    800.00,         12],
    [800.01,    1200.00,        10],
    [1200.01,   2000.00,        7],
    [2000.01,   Infinity,       4],
]

for(const line of table_salary_readjustment_rate){
    if(line[0] <= salary && salary <= line[1]){
        const per = line[2]
        const readjust = (salary * per) / 100.0
        const newSalary = salary + readjust

        console.log(`Novo salario: ${newSalary.toFixed(2)}`)
        console.log(`Reajuste ganho: ${readjust.toFixed(2)}`)
        console.log(`Em percentual: ${per} %`)
    }
}