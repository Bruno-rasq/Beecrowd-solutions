<?php

$inputs = fopen("php://stdin", "r");

function DFS(&$visitados, $grafico, $node) {
    $visitados[$node] = true;

    if (!isset($grafico[$node])) {
        return;
    }

    foreach ($grafico[$node] as $vizinho) {
        if (!isset($visitados[$vizinho])) {
            DFS($visitados, $grafico, $vizinho);
        }
    }
}

while (($data = fgets($inputs)) !== false) {
    $data = trim($data);
    if (empty($data)) continue;

    list($leds, $segmentos) = explode(" ", $data);
    $leds = (int) $leds;
    $segmentos = (int) $segmentos;

    $grafico = [];
    $visitados = [];

    for ($i = 0; $i < $segmentos; $i++) {
        $linha = trim(fgets($inputs));
        list($n, $m) = explode(" ", $linha);
        $n = (int) $n;
        $m = (int) $m;

        if (!isset($grafico[$n])) $grafico[$n] = [];
        if (!isset($grafico[$m])) $grafico[$m] = [];

        $grafico[$n][] = $m;
        $grafico[$m][] = $n;
    }

    DFS($visitados, $grafico, 1);

    echo count($visitados) === $leds ? "COMPLETO\n" : "INCOMPLETO\n";
}
