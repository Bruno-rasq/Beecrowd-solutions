<?php 
    $a = (float) readline() * 2.0;
    $b = (float) readline() * 3.0;
    $c = (float) readline() * 5.0;

    $average = ($a + $b + $c) / 10.0;
    $formated = number_format($average, 1, ".", "");

    echo "MEDIA = $formated\n";

?>