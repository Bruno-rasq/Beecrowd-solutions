const fs = require('fs')
const input = fs.readfileSync('/dev/stdin', 'utf-8')
const lines = input.split('\n')

const ascii = (list) => {
    let dict = {}
    list.forEach(char => {
        let charcode = char.charCodeAt(0)
        if(dict[charcode]){
            dict[charcode] += 1
        } else {
            dict[charcode] =  1
        }
    })

    return Object.entries(dict).map(([key, value]) => [parseInt(key), value])
}

const sortedmatrix = (matrix ) => {
    return matrix.sort((a, b) => {
        if(a[1] == b[1]){
            return b[0] - a[0]
        }
        return a[1] - b[1]
    })
}

const output = (matrix) => {
    matrix.forEach(line => {
        console.log(lines.join(' '))
    })
}

lines.forEach((line, index) => {
    let curr = line.split(' ')
    let matrix = ascii(curr)
    let srotedmatrix = sortedmatrix(matrix)

    outpur(srotedmatrix)

    if(index < lines.length - 1){
        console.log()
    }
})