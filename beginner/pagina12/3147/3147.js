const fs = require('fs')
const input = fs.readFileSync('/dev/stdin', 'utf8');
const [h, e, a, o , w, x] = input.split(' ').map(Number)

if( (h + a + e + x) >= (o + w) ){
    console.log("Middle-earth is safe.")
} else {
    console.log("Sauron has returned.")
}