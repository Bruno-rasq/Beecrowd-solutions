const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')


lines.forEach(line => {
    let data = Number(line)

    if(!isNaN(data) && line.trim() !== ""){
        if(data <= 100){
            console.log(1)

        } else {
            let seculo = Math.floor(data / 100)
            if(data % 100 != 0){
                seculo++
            }
            console.log(seculo)
        }
    }
})