<?php 

    $x = (int) readline();
    $y = (float) readline();

    $average = number_format(($x / $y), 3, ".", "");

    echo "$average km/l\n";

?>