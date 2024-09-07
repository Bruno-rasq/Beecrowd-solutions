<?php 

    $a = (float) readline();
    $pi = 3.14159;

    $area = $pi * ($a * $a);

    echo "A=" . number_format($area, 4, ".", "") . "\n";

?>