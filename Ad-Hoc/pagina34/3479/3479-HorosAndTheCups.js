console.log(" 3479 - Horo and the cups ");

const input = `26/02`;

let lines = input.split('\n');
let [ day, mon ] = lines.shift().split('/').map(el => Number(el))

function horos(d, m){

    if(m === 1){
        if(d <= 19) console.log('capricornio')
        if(d >= 20) console.log('aquario')

    } else if(m === 2){
        if(d <= 18) console.log('aquario')
        if(d >= 19) console.log('peixes')

    } else if(m === 3){
        if(d <= 20) console.log('peixes')
        if(d >= 21) console.log('aries')

    } else if(m === 4){
        if(d <= 20) console.log('aries')
        if(d >= 21) console.log('touro')

    } else if(m === 5){
        if(d <= 20) console.log('touro')
        if(d >= 21) console.log('gemeos')
        
    } else if(m === 6){
        if(d <= 20) console.log('gemeos')
        if(d >= 21) console.log('cancer')
        
    } else if(m === 7){
        if(d <= 22) console.log('cancer')
        if(d >= 23) console.log('leao')
        
    } else if(m === 8){
        if(d <= 22) console.log('leao')
        if(d >= 23) console.log('virgem')
        
    } else if(m === 9){
        if(d <= 22) console.log('virgem')
        if(d >= 23) console.log('libra')
        
    } else if(m === 10){
        if(d <= 22) console.log('libra')
        if(d >= 23) console.log('escorpiao')
        
    } else if(m === 11){
        if(d <= 21) console.log('escorpiao')
        if(d >= 22) console.log('sargitario')
        
    } else if(m === 12){
        if(d <= 21) console.log('sargitario')
        if(d >= 22) console.log('capricornio')
        
    };
};

horos(day, mon)