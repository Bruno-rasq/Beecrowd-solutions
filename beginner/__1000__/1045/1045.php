<?php 

    /**
     * FUNCIONA MAS O SITE ME BLOQUEOU! KK
     */

    function bubbleSort($lista){
        $len = count($lista);
        for($i = 0; $i < $len; $i++){
            for($j = 0; $j < $len - $i - 1; $j++){
                if($lista[$j] > $lista[$j + 1]){
                    $temp = $lista[$j + 1];
                    $lista[$j + 1] = $lista[$j];
                    $lista[$j] = $temp;
                }
            }
        }
        return $lista;
    }

    $INPUT = explode(" ", readline());
    $data = [];
    for($i = 0; $i < 3; $i++){
        $data[$i] = (float) $input[$i];
    }

    list($C, $B, $A) = bubbleSort($data);

    $a2 = $A * $A;
    $bc2 = ($B * $B) + ($C * $C);

    if($A >= $B + $C) echo "NAO FORMA TRIANGULO\n";
    else {
        if(abs($a2 - $bc2) < 0.000000001 ) echo "TRIANGULO RETANGULO\n";
        if($a2 > $bc2) echo "TRIANGULO OBTUSANGULO\n";
        if($a2 <  $bc2) echo "TRIANGULO ACUTANGULO\n";
        if($A == $B && $B == $C) echo "TRIANGULO EQUILATERO\n";
        else if($A == $B || $A == $C || $C == $B){
            echo "TRIANGULO ISOSCELES\n";
        }
    }
?>