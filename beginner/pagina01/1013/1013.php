<?php 

    function maior($a, $b){
        return ($a + $b + abs($a - $b)) / 2;
    }

    list($a, $b, $c) = explode(' ', readline());
    $a = (int) $a;
    $b = (int) $b;
    $c = (int) $c;

    $maior = maior($a, maior($b, $c));

    echo "$maior eh o maior\n";
?>