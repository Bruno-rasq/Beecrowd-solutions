<?php 

    list($a, $b) = explode(" ", readline());

    $a = (float) $a;
    $b = (float) $b;

    $result = (
        ((1.0 + $a / 100) * (1.0 + $b / 100)) - 1.0
    ) * 100;
    $fomated = number_format($result, 6, '.', '');

    echo "$formated\n";
    
?>