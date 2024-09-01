<?php 

    $a = fgets(STDIN);
    $b = fgets(STDIN);
    $c = fgets(STDIN);
    $d = fgets(STDIN);
    $e = fgets(STDIN);

    $cassava = ($a * 300) + ($b * 1500) + ($c * 600) + ($d * 1000) + ($e * 150) + 225;

    echo $cassava . "\n";

?>