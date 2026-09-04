<?php 

    $moeda = (float) readline();
    $q = (int) readline();

    $result = $moeda * $q;
    $valor = number_format($result, 2, '.','');

    echo "$valor\n";

?>