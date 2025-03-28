<?php

$nome = readline();
list($a, $b, $c) = explode("/", readline());
list($d, $e, $f) = explode("/", readline());

$dia_atual = (int) $a; $mes_atual = (int) $b; $ano_atual = (int) $c;
$dia_nasci = (int) $d; $mes_nasci = (int) $e; $ano_nasci = (int) $f;

$idade = $ano_atual - $ano_nasci;

if($dia_atual == $dia_nasci && $mes_atual == $mes_nasci){
    echo "Feliz aniversario!\n";
}

if($mes_atual < $mes_nasci || ($mes_atual == $mes_nasci && $dia_atual < $dia_nasci)){
    $idade -= 1;
}

echo "Voce tem $idade anos $nome.\n";