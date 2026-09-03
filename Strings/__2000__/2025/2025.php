<?php

function corrigirPalavra($palavra) {
    if (strlen($palavra) == 10 && substr($palavra, 1, 8) === "oulupukk") {
        return "Joulupukki";
    } elseif (strlen($palavra) == 11 && substr($palavra, 1, 8) === "oulupukk" && substr($palavra, -1) === ".") {
        return "Joulupukki.";
    }
    return $palavra;
}

$handle = fopen("php://stdin", "r");
$n = intval(fgets($handle));

for ($i = 0; $i < $n; $i++) {
    $linha = trim(fgets($handle));
    $mensagem = explode(" ", $linha);
    $corrigida = [];

    foreach ($mensagem as $palavra) {
        $corrigida[] = corrigirPalavra($palavra);
    }

    echo implode(" ", $corrigida) . "\n";
}

fclose($handle);
