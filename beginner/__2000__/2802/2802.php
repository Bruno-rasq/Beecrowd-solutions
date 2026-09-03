<?php 

    $n = (int) readline();

    $partA = (($n - 1) * $n) / 2;
    $partB = ($n * ($n - 1) * ($n - 2) * ($n - 3)) / 24;

    $segmentos = 1 +  $partA + $partB;

    echo "$segmentos\n";

?>