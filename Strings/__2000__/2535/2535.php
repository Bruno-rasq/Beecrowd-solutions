<?php

function inicial($inicial_raca, $nome) {
    foreach ($nome as $parte) {
        if ($parte[0] === $inicial_raca) {
            return true;
        }
    }
    return false;
}

while (($n = intval(readline())) !== 0) {

    $pets = 0;
    for ($i = 0; $i < $n; $i++) {
        $especie = trim(readline());
        $raca = trim(readline());
        $nome = explode(" ", trim(readline()));
        readline(); // linha em branco

        if (
            $especie === "cachorro" &&
            count($nome) > 1 &&
            inicial($raca[0], $nome)
        ) {
            $pets++;
        }
    }

    echo "$pets\n";
}