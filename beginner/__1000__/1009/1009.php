<?php 
    $numero = (string) readline();
    $salario = (int) readline();
    $vendidos = (float) readline();

    $bonus = ($vendidos * 15) / 100;
    $salario = number_format(($salario + $bonus), 2, ".", '');

    echo "TOTAL = R$ $salario\n";
?>