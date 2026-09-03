<?php

function hamming_distance($str1, $str2){
    $distance = 0;
    for($i = 0; $i < strlen($str1); $i++){
        if($str1[$i] !== $str2[$i]) $distance++;
    }
    return $distance;
}

$str1 = trim(readline());
$k = (int) trim(readline());

$indice = -1;
$menor_distance = INF;

for($i = 0; $i < 5; $i++){
    $str2 = trim(readline());

    $distance = hamming_distance($str1, $str2);
    if($distance < $menor_distance){
        $menor_distance = $distance;
        $indice = $i + 1;
    }
}

echo $indice . "\n";
echo ($menor_distance <= $k ? $menor_distance : -1) . "\n";
