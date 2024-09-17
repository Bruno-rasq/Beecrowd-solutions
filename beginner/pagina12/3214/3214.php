<?php 

    list($e, $g, $f) = explode(" ", readline());

    $e = (int) $e;
    $g = (int) $g;
    $f = (int) $f;

    $count = 0;
    $e = $e + $g;
    while($e >= $f){
        $e = ($e - $f + 1);
        $count++;
    }

    echo "$count\n";
?>