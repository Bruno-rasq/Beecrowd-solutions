<?php

$notas = [];
$n = (int) readline();

for($i = 0; $i < $n; $i++){
    $curr = (int) readline();
    $notas[$curr] = true;
}

$len = count($notas);
echo "$len\n";