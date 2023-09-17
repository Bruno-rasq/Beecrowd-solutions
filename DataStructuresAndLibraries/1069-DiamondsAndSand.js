console.log(" 1069 - Diamonds and Sand ");

const input = `3
.>><..<<<>.<.>>..>...<<.>....

<>`;

let lines = input.split('\n');
let int = Number(lines.shift());


for ( let i = 0; i < int; i++ ){

    let dataPrime = lines[i].split('');

    let data = dataPrime.filter(item => {
        return item == "<" || item == ">"
    });


    let diamonds = 0;
    let aux = 0;

    for ( let n = 0; n < data.length; n++ ){

        if(data[n] == "<"){
            aux++

        } else if (data[n] == ">"){
            if(aux > 0){
                aux--
                diamonds++
            }
        }
    }
   
    console.log(diamonds)
};




// console.log(" 1069 - Diamonds and Sand ");

// const input = `3
// .>><..<<<>.<.>>..>...<<.>....

// <>`;

// let lines = input.split('\n');
// let int = Number(lines.shift());


// for ( let i = 0; i < int; i++ ){

//     let dataPrime = lines[i].split('');

//     let open = dataPrime.filter(item => {
//         return item == "<" 
//     });

//     let close = dataPrime.filter(item => {
//         return item == ">"
//     });


//     let Intercalate = undefined;
//     if(open.length !== null && close.length !== null){
//         Intercalate = intercale(open, close);
//     };


//     let diamonds = 0;
//     for ( let n = 0; n < Intercalate.length; n+=2 ){

//         if(Intercalate[n] == "<" && Intercalate[n+1] == ">"){
//             diamonds++
//         }
//     }
   
//     console.log(Intercalate, diamonds)
// };


// function intercale(array1, array2) {

//     let arrayResult = [];
//     let total = 0;

//     if (array1.length > array2.length) {
//       total = array1.length;

//     } else {
//       total = array2.length;
//     }
  
//     for (let i = 0; i < total; i++) {
//       if (array1[i]) {
//         arrayResult.push(array1[i]);
//       }
//       if (array2[i]) {
//         arrayResult.push(array2[i]);
//       }
//     }
  
//     return arrayResult;
//   };