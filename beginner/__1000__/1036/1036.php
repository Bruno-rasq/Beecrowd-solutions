<?php

$entrada = trim(fgets(STDIN));
$valores = explode(" ", $entrada);

$A = (float)$valores[0];
$B = (float)$valores[1];
$C = (float)$valores[2];

$delta = $B * $B - 4 * $A * $C;

if ($A != 0 && $delta >= 0) {
    $R1 = (-$B + sqrt($delta)) / (2 * $A);
    $R2 = (-$B - sqrt($delta)) / (2 * $A);

    printf("R1 = %.5f\n", $R1);
    printf("R2 = %.5f\n", $R2);
} else {
    echo "Impossivel calcular\n";
}
?>
