<?php 

    $num = (int) readline();

    $horas = (int) ($num / 3600);
    $minutos = (int) (($num % 3600) / 60);
    $segundos = (int) $num % 60;

    echo "$horas:$minutos:$segundos\n";
    
?>
