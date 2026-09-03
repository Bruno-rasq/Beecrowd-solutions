<?php 
    $numero = (int) readline();
    $horas = (int) readline();
    $valor = (float) readline();
   

    $salario = number_format($horas * $valor, 2, ".", '');


    echo "NUMBER = $numero\n";
    echo "SALARY = U$ $salario\n";
?>