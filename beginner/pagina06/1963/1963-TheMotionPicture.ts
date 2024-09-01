const input = `20.00 30.00`
const lines = input.split(' ').map(element => parseFloat(element))

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
// const lines = input.split('\n')

const The_motion_picture = (nums: number[]): void => {
    let [Pa, Pn] = nums
    let diff = Pn - Pa
    let response = (diff * 100) / Pa

    console.log(`${response.toFixed(2)}%`)

}

The_motion_picture(lines)