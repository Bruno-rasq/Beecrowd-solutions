<?php 

    $tempo = (int) readline();
    $kmh = (int) readline();

    $response = ($tempo * $kmh) / 12;

    echo number_format($response, 3, ".", '') . "\n";

?>