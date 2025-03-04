<?php
$lista_atual = explode(" ", trim(fgets(STDIN)));
$nova_lista = explode(" ", trim(fgets(STDIN)));
$amigo_indicado = trim(fgets(STDIN));

$lista_atualizada = [];

if ($amigo_indicado != "nao" && in_array($amigo_indicado, $lista_atual)) {
    foreach ($lista_atual as $amigo) {
        if ($amigo == $amigo_indicado) {
            foreach ($nova_lista as $amigo_novo) {
                $lista_atualizada[] = $amigo_novo;
            }
        }
        $lista_atualizada[] = $amigo;
    }
} else {
    $lista_atualizada = array_merge($lista_atual, $nova_lista);
}

echo implode(" ", $lista_atualizada) . "\n";