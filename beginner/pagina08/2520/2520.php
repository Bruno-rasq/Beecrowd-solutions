<?php

while (($case = fgets(STDIN)) !== false) {

    list($n, $m) = explode(" ", trim($case));

    $X = [0, 0];
    $Y = [0, 0];

    for ($i = 0; $i < (int)$n; $i++) {
        $linha = explode(" ", trim(fgets(STDIN)));
        for ($j = 0; $j < (int)$m; $j++) {
            if ($linha[$j] === "1") $X = [$i, $j];
            if ($linha[$j] === "2") $Y = [$i, $j];
        }
    }

    $dist = abs($X[0] - $Y[0]) + abs($X[1] - $Y[1]);
    echo "$dist\n";
}