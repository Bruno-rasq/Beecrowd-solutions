<?php

function toBinaryString($n){
    if($n == 0) return "0";
    $bin = "";
    while ($n > 0){
        $bin = ($n % 2 ? "0" : "1") + $bin;
        $n /= 2;
    }
    return $bin;
}

$mnv = 0;
for($i = 0; $i < 4; $i++){
    $soma = 0;
    $data = explode(" ", readline());
    for($j = 0; $j < 7; $j++){
        $soma += $data[$j];
    }
    if($soma > $mnv) $mnv = $soma;
}

$bin = toBinaryString($mnv);
echo "$mnv = $bin\n";