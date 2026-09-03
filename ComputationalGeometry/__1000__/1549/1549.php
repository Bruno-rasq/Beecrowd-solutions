<?php

$n = (int) readline();
for($i = 0; $i < $n; $i++){

    list($pessoas, $mililitros) = explode(" ", readline());
    list($b, $B, $H) = explode(" ", readline());

    $b = (int) $b; $B = (int) $B; $H = (int) $H;

    $media = (int) $mililitros / (int) $pessoas;
    $temp = pow(($media * 3 * ($B - $b) / (pi() * $H)) + pow($b, 3), (1/3));
    $h = $media * 3 / (pi() * (pow($temp, 2) + $temp * $b + pow($b, 2)));

    echo number_format($h, 2, ".", "") . "\n";
}