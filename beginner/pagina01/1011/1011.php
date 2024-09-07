<?php 
    $r = (float) readline();
    $pi = 3.14159;

    $volume = ($r * $r * $r) * $pi * (4.0/3.0);
    $volume = number_format($volume, 3, ".", '');

    echo "VOLUME = $volume\n";

?>