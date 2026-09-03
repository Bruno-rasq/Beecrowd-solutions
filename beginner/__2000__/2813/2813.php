<?php 

    $n = (int) readline();

    $guardachuvaCasa = 0;
    $guardachuvatrabalho = 0;
    $comprasCasa = 0;
    $comprasTrabalho = 0;

     for($i = 0; $i < $n; $i++){

        list($ida, $volta) = explode(" ", readline());

        if($ida == "chuva"){
            $guardachuvaCasa > 0 ? $guardachuvaCasa-- : $comprasCasa++;
            $guardachuvatrabalho++;
        }

        if($volta == "chuva"){
            $guardachuvatrabalho > 0 ? $guardachuvatrabalho-- : $comprasTrabalho++;
            $guardachuvaCasa++;
        }
     }

     echo "$comprasCasa $comprasTrabalho\n";

?>