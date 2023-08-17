
function TimeConvert(n){

    let hours = Math.floor(n / 3600);
    let minu = Math.floor((n - (hours * 3600)) / 60);
    let second = Math.floor(n % 60);

    console.log(`${hours.toFixed(0)}:${minu.toFixed(0)}:${second}`);
   
}

TimeConvert(556);
TimeConvert(1);
TimeConvert(140153);