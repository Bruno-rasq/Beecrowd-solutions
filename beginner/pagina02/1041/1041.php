<?php 

    list($a, $b) = explode(" ", readline());
    $a = (float) $a; $b = (float) $b;

    if($a === 0 && $b === 0){echo "Origem\n";}
    else if ($a == 0){echo "Eixo Y\n";}
    else if ($b == 0){echo "Eixo X\n";}
    else if ($b > 0 && $a > 0){echo "Q1\n";}
    else if ($b > 0 && $a < 0){echo "Q2\n";}
    else if ($b < 0 && $a < 0){echo "Q3\n";}
    else if ($b < 0 && $a > 0){echo "Q4\n";}

?>