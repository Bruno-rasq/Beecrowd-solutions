console.log(" 1022 - TDA rational");

function test(str){

    let split = str.split("+");

    let arry1 = split[0].split("/");
    let [ n1, d1 ] = arry1.map(item => parseFloat(item));

    let arry2 = split[1].split("/");
    let [ n2, d2 ] = arry2.map(item => parseFloat(item));

    console.log(str)
    console.log(n1, n2, d1, d2)
    
}

test("1/2 + 3/4");
