<?php

function wordPlay($palavra, $i){
    $menor = $palavra;
    $maior = $palavra;
    $dupla = $palavra + $palavra;

    for ($j = 1; $j < strlen($palavra); $j++) {
        $rotacionada = substr($dupla, $j, strlen($palavra));

        if ($rotacionada < $menor) $menor = $rotacionada;
        if ($rotacionada > $maior) $maior = $rotacionada;
    }

    echo "Caso $i: $menor $maior\n";
}

$i = 1;
while(($palavra = readline()) != "*"){
    wordPlay($palavra, $i);
    $i++;
}