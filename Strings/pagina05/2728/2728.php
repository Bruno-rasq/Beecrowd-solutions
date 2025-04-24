<?php

while ($linha = readline()) {
    $palavras = explode("-", $linha);

    $cobol = "cobol";
    $valido = true;

    foreach ($palavras as $i => $palavra) {
        $char = $cobol[$i];
        $letraInicial = $palavra[0] ?? '';
        $letraFinal = $palavra[strlen($palavra) - 1] ?? '';

        if (strcasecmp($letraInicial, $char) !== 0 && strcasecmp($letraFinal, $char) !== 0) {
            $valido = false;
            break;
        }
    }

    echo $valido ? "GRACE HOPPER\n" : "BUG\n";
}
