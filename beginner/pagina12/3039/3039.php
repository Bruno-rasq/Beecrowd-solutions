<?php 
    $n = (int) readline();
    $carrinhos = 0; $bonecas = 0;

    for($i = 0; $i < $n; $i++){
        list($nome, $sexo) = explode(" ", readline());

        if($sexo == "M"){ $carrinhos += 1;}
        else { $bonecas += 1;}
    }

    echo "$carrinhos carrinhos\n";
    echo "$bonecas bonecas\n";
?>