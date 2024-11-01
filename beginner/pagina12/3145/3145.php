<?php 

    list($hobbits, $km) = explode(" ", readline());

    $hobbits = (int) $hobbits;
    $km = (double) $km;

    $result = $km / $hobbits;
    $response = number_format($result, 2, ".", "");

    echo "$response\n";
?>