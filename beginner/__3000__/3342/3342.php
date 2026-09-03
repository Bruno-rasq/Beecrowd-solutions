<?php 

    $n = (int) readline();

    $total_cases = $n * $n;
    $b = 0; $p = 0;

    if ($n % 2 == 0){
        $b = $total_cases / 2;
        $p = $total_cases / 2;
    } else {
        $b = ($total_cases + 1) / 2;
        $p = $b - 1;
    }

    echo "$b casas brancas e $p casas pretas\n";
?>