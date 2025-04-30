<?php

 $valor_limite =  2147483647;

 while(($line = readline()) != false){

    $num = "";
    $is_valide = true;

    for($i = 0; $i < strlen($line); $i++){
        $chr = $line[$i];

        if ($chr >= '0' && $chr <= '9') {
            $num += $ch;
        } else if ($chr == 'O' || $chr == 'o') {
            $num += '0';
        } else if ($chr == 'l') {
            $num += '1';
        } else if ($chr == ' ' || $chr == ',') {
            continue;
        } else {
            $isValid = false;
            break;
        }
    }

    $error = $num == "" || (int) $num > $valor_limite;
    echo !$error && $is_valide ? $num : "error" . "\n";
 }