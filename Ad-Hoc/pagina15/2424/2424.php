<?php

list($x, $y) = explode(" ", readline());
$x = (int) $x;
$y = (int) $y;

$condicao = $x >= 0 && $x <= 432 && $y >= 0 && $y <= 468;
if($condicao){echo "dentro\n";} else {echo "fora\n";}