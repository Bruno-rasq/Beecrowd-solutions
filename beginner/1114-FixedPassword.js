console.log(" 1114 - Fixed password ");

const input = `2200
2002
2022
2002`;

let lines = input.split('\n')

let logs = []
let i = 0
let password = 'Senha Invalida'

while(password == 'Senha Invalida'){

    if(lines[i] == '2002'){
        password = 'Acesso Permitido'
    }
    logs.push(password)
    i++

}

console.log(logs.join('\n'))