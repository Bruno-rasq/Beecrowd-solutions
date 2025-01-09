<?php 

    list($voltas, $placas) = explode(" ", readline());

    $voltas = (int) $voltas;
    $placas = (int) $placas;

    $total_placas = $voltas * $placas;

    $results = [];

    for($i = 10; $i <= 90; $i += 10){
        $qnt_placas_por_porcentagem = ceil(($total_placas * $i) / 100);
        $results[] = $qnt_placas_por_porcentagem;
    }

    $output = implode(" ", $results);

    echo "$output\n";
?>