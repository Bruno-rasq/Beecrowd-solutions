<?php
    $n = intval(fgets(STDIN));

    $cen = floor($n / 100);
    $rest100 = $n % 100;

    $cin = floor($rest100 / 50);
    $rest50 = $rest100 % 50;

    $vin = floor($rest50 / 20);
    $rest20 = $rest50 % 20;

    $dez = floor($rest20 / 10);
    $rest10 = $rest20 % 10;

    $cinco = floor($rest10 / 5);
    $rest5 = $rest10 % 5;

    $dois = floor($rest5 / 2);
    $rest2 = $rest5 % 2;

    $um = floor($rest2);

    echo "$n\n";
    echo "$cen nota(s) de R$ 100,00\n";
    echo "$cin nota(s) de R$ 50,00\n";
    echo "$vin nota(s) de R$ 20,00\n";
    echo "$dez nota(s) de R$ 10,00\n";
    echo "$cinco nota(s) de R$ 5,00\n";
    echo "$dois nota(s) de R$ 2,00\n";
    echo "$um nota(s) de R$ 1,00\n";
?>
