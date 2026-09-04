<?php

list($a, $b) = explode(" ", readline());
$trocas = explode(" ", readline());

$volume_atual = (int) $a; 
$n = (int) $b;

for($i = 0; $i < $n; $i++){
    $ALT = (int) $trocas[$i];
    $novo_volume = max(0, min(100, $volume_atual + $ALT));
    $volume_atual = $novo_volume;
}

echo "$volume_atual\n";