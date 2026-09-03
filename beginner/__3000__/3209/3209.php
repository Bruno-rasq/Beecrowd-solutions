<?php 

    $n = (int) readline();

    for($i = 0; $i < $n; $i++){
        $data = explode(" ", readline());

        $t = (int) $data[0];
        $reguas = array_map('intval', array_slice($data, 1));

        $total = $reguas[0];

        for($j = 0; $j < $t; $j++){
            $total = ($total - 1) + $reguas[$j];
        }
        echo "$total\n";
    }
?>