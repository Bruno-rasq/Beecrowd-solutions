<?php 

    list($a, $b) = explode(" ", readline());

    $a = (int) $a;
    $b = (int) $b;

    if($a < $b){
        $temp = $b;
        $b = $a;
        $a = $temp;
    }

    if($a % $b == 0){
        echo "Sao Multiplos\n";
    } else {

        echo "Nao sao Multiplos\n";
    }
?>