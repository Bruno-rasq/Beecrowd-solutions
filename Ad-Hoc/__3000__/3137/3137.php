<?php

$n = (int) readline();
$total = 0;
$casas = [1000000, 100000, 10000, 1000, 100, 10, 1];

for($i = 0; $i < 7; $i++){
    $casa = $casas[$i];
    if($n >= $casa){
        $qnt = $n - $casa + 1;
        $digitos = strlen((string) $casa);
        $total += $qnt * $digitos;
        $n = $casa - 1;
    }
}

echo "$total\n";