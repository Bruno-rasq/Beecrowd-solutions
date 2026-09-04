const input = `Flowers Flourish from France
Sam Simmonds speaks softly
Peter pIckEd pePPers
truly tautograms triumph
this is NOT a tautogram
*`;

// const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const lines = input.split('\n');

const IsTautogram = (phrase: string[]): void => {

   let firstChars = phrase.map((word) => {
        let aux = word.toLowerCase().split('')
        return aux[0]
   })

   let initialChar = firstChars.shift()

   let response = firstChars.every(function(char: string){
        return char == initialChar 
   })

   console.log(response ? 'Y' : 'N')
}

const Setup = (datas: string[]): void => {

    for(let i = 0; i < datas.length; i++){
        let data = datas[i]
        
        if(data == '*') break

        IsTautogram(data.split(' '))
    }
}

Setup(lines)