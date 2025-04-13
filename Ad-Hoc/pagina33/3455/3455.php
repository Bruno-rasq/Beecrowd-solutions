<?php

$linha1 = explode(" ", trim(fgets(STDIN)));
$grafica = (float) $linha1[0];
$dinamica = (float) $linha1[1];
$geometrica = (float) $linha1[2];

$tipo = trim(fgets(STDIN));

$total = 0.0;

if ($tipo === "A") {
    $total += $grafica;
    $total += $dinamica * (3.0 / 2.0);
    $total += $geometrica * 2.5;
} elseif ($tipo === "B") {
    $total += $dinamica;
    $total += $grafica * (2.0 / 3.0);
    $total += $geometrica * 2.5 * (2.0 / 3.0);
} elseif ($tipo === "C") {
    $total += $geometrica;
    $total += $grafica * (1.0 / 2.5);
    $total += $dinamica * (3.0 / 2.0) * (1.0 / 2.5);
}

echo intval(floor($total)) . "\n";