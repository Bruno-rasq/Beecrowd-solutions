<?php 

    list($a, $b) = explode(' ', readline());
    $a = (int) $a;
    $b = (int) $b;

    if($a > $b){
        echo "{$a}\n";
    } else {
        echo "{$b}\n";
    }

?>