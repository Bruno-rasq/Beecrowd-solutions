<?php 
    $a = fgets(STDIN) * 3.5;
    $b = fgets(STDIN) * 7.5;

    $average = ($a + $b) / 11;
    $Format = number_format($average, 5, ".", "");

    echo "MEDIA = $Format\n";
?>