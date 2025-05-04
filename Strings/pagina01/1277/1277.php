<?php

$casos = (int)fgets(STDIN);

for ($i = 0; $i < $casos; $i++) {
    $n_alunos = (int)fgets(STDIN);
    $alunos = explode(" ", trim(fgets(STDIN)));
    $frequencias = explode(" ", trim(fgets(STDIN)));
    $output = [];

    for ($j = 0; $j < $n_alunos; $j++) {
        $nome = $alunos[$j];
        $freq = $frequencias[$j];

        $total = 0;
        $faltas = 0;

        $chars = str_split($freq);
        foreach ($chars as $c) {
            if ($c === 'M') continue;
            if ($c === 'A') $faltas++;
            $total++;
        }

        if ($total === 0) continue; // evita divisão por zero

        $presencas = $total - $faltas;
        $porcentagem = ($presencas * 100) / $total;

        if ($porcentagem < 75) {
            $output[] = $nome;
        }
    }

    echo implode(" ", $output) . PHP_EOL;
}