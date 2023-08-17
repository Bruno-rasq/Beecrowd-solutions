function bankNotesWithCoins(n) {

    // notes
    let cen = Math.floor(n / 100);
    let rest100 = n % 100;

    let cin = Math.floor(rest100 / 50);
    let rest50 = rest100 % 50;

    let vin = Math.floor(rest50 / 20);
    let rest20 = rest50 % 20;

    let dez = Math.floor(rest20 / 10);
    let rest10 = rest20 % 10;

    let cinco = Math.floor(rest10 / 5);
    let rest5 = rest10 % 5;

    let dois = Math.floor(rest5 / 2);
    let rest2 = rest5 % 2;

    let um = Math.floor(rest2 / 1);
    let rest1 = rest2 % 1

    // coins
    let cent50 = Math.floor(rest1 / 0.50);

    let cent25 = Math.floor((rest1 - (0.50 * cent50)) / 0.25);

    let cent10 = Math.floor((rest1 - (0.50 * cent50) - (0.25 * cent25)) / 0.10);

    let cent5 = Math.floor((rest1 - (0.50 * cent50) - (0.25 * cent25) - (0.10 * cent10)) / 0.05);

    let cent1 = Math.floor((rest1 - (0.50 * cent50) - (0.25 * cent25) - (0.10 * cent10) - (0.05 * cent5)) / 0.01)


    console.log("NOTAS:");
    console.log(`${cen.toFixed(0)} nota(s) de R$ 100.00`);
    console.log(`${cin.toFixed(0)} nota(s) de R$ 50.00`);
    console.log(`${vin.toFixed(0)} nota(s) de R$ 20.00`);
    console.log(`${dez.toFixed(0)} nota(s) de R$ 10.00`);
    console.log(`${cinco.toFixed(0)} nota(s) de R$ 5.00`);
    console.log(`${dois.toFixed(0)} nota(s) de R$ 2.00`);

    console.log("MOEDAS:");
    console.log(`${um.toFixed(0)} moeda(s) de R$ 1.00`);
    console.log(`${cent50.toFixed(0)} moeda(s) de R$ 0.50`);
    console.log(`${cent25.toFixed(0)} moeda(s) de R$ 0.25`);
    console.log(`${cent10.toFixed(0)} moeda(s) de R$ 0.10`);
    console.log(`${cent5.toFixed(0)} moeda(s) de R$ 0.05`);
    console.log(`${cent1.toFixed(0)} moeda(s) de R$ 0.01`);

}

bankNotesWithCoins(576.73);
bankNotesWithCoins(4);
bankNotesWithCoins(91.09);

