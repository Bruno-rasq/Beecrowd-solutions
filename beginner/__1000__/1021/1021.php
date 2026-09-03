<?php

    $notas = [10000, 5000, 2000, 1000, 500, 200];
    $moedas = [100, 50, 25, 10, 5, 1];

    list($reais, $centavos) = explode('.', readline());

    $reais = (int) $reais;
    $centavos = (int) $centavos;
    
    $reais = $reais * 100 + $centavos;

    echo "NOTAS:\n";
    for ($i = 0; $i < 6; ++$i) {
        echo intval($reais / $notas[$i]) . " nota(s) de R$ " . number_format($notas[$i] / 100, 2, '.', '') . "\n";
        $reais %= $notas[$i];
    }

    echo "MOEDAS:\n";
    for ($i = 0; $i < 6; ++$i) {
        echo intval($reais / $moedas[$i]) . " moeda(s) de R$ " . number_format($moedas[$i] / 100, 2, '.', '') . "\n";
        $reais %= $moedas[$i];
    }

?>