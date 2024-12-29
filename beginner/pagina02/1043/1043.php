<?php 

    list($A, $B, $C) = explode(" ", readline());

    $A = (float) $A;
    $B = (float) $B;
    $C = (float) $C;

    $perimetro = ($A + $B + $C);
    $area = (($A + $B) * $C ) / 2;
    $condicao = $A < ($B + $C) && $B < ( $A + $C) && $C < ($A + $B);

    $response_p = number_format($perimetro, 1, ".", "");
    $response_A = number_format($area, 1, ".", "");

    if($condicao){
        echo "Perimetro = $response_p\n";
    } else {
        echo "Area = $response_a\n";
    }

?>