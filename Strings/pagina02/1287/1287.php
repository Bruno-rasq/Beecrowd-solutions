<?php

$valor_limite = 2147483647;

while (($line = readline()) !== false) {
    $num = "";
    $is_valide = true;

    for ($i = 0; $i < strlen($line); $i++) {
        $chr = $line[$i];

        if ($chr >= '0' && $chr <= '9') {
            $num .= $chr;
        } else if ($chr == 'O' || $chr == 'o') {
            $num .= '0';
        } else if ($chr == 'l') {
            $num .= '1';
        } else if ($chr == ' ' || $chr == ',') {
            continue;
        } else {
            $is_valide = false;
            break;
        }
    }

    $error = $num === "" || (int)$num > $valor_limite || !$is_valide;
    echo !$error ? (int)$num . "\n" : "error\n";
}