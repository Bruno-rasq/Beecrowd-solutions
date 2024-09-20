<?php 

    $raio = (float) readline();
    $pi = 3.14;
    $circunferencia = 2 * ($raio * $pi);

    $fomated = number_format($circunferencia, 2, ".", '');

    echo "$formated\n";
?>