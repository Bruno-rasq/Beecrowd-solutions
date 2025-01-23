<?php 

    list($porcent1, $porcent2) = explode(" ", readline());

    $porcent1 = (int) $porcent1;
    $porcent2 = (int) $porcent2;

    if ( $porcent2 <= 2 && $porcent2 >= 0 )
        echo "nova\n";

    else if ( $porcent2 <= 100 && $porcent2 >= 97 )
        echo "cheia\n";

    else if ( $porcent1 < $porcent2)
        echo "crescente\n";

    else 
        echo "minguante\n"; 
?>