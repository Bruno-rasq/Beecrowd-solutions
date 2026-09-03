<?php 
    list($code1, $qnt1, $valor1) = explode(' ', readline());
    list($code2, $qnt2, $valor2) = explode(' ', readline());

    $qnt1 = (int) $qnt1;
    $qnt2 = (int) $qnt2;

    $valor1 = (float) $valor1;
    $valor2 = (float) $valor2;

    $total = ($qnt1 * $valor1) + ($qnt2 * $valor2);
    $totalformated = number_format($total, 2, ".", '');

    echo "VALOR A PAGAR: R$ $totalformated\n";
?>