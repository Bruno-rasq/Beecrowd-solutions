<?php 

    list($qt, $litros, $refill) = explode(" ", readline());

    $lista = explode(" ", readline());

    $litros = (float) $litros;
    $refill = (float) $refill;

    $rico = '';
    $index = 0;

    while($litros > $refill){
        $litros -= $refill;
        $rico = $lista[$index];
        $index = ($index + 1) % count($lista);
    }

    $rico = $lista[$index];

    echo "$rico " . number_format($litros, 1, ".", '') . "\n";
?>