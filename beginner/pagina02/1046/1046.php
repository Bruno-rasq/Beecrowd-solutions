<?php 

    list($start, $end) = explode(' ', readline());
    $start = (int) $start;
    $end = (int) $end;
    $time;

    if($start < $end){
        $time = $end - $start;
    } else {
        $time = (24 - $start) + $end;
    }

    echo "O JOGO DUROU {$time} HORA9(S)\n";

?>