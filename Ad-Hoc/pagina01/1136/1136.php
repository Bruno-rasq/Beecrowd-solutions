<?php

while(true){

    list($n, $b) = explode(" ", readline());
    $n = (int) $n;
    $b = (int) $b;

    if($n == 0 && $b == 0) break;

    $bolas = explode(" ", readline());
    $possibilidades = [];
    $possibilidades[0] = true;

    for($i = 0; $i < $b; $i++){
        for($j = $i + 1; $j < $b; $j++){
            $diff = abs((int)$bolas[$i] - (int)$bolas[$j]);
            $possibilidades[$diff] = true;
        }
    }

    if(sizeof($possibilidades) == $n + 1){
        echo "Y\n";
    } else {
        echo "N\n";
    }
}