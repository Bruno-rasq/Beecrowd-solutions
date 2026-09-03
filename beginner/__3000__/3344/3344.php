<?php 

    $n = (int) readline();

    $unitarios = [
        4, 3, 3, 5, 4, 4, , 3, 5, 5, 4, 3,
        6, 6, 8, 8, 7, 7, 9, 8, 8, 6
    ];

    $decimais = [6, 6, 5, 5, 5, 7, 6, 6];

    for($i = 0; $i < 1000; $i++){
        if($n == 100){ $n = 11; }
        else if ($n <= 20){ $n = $unitarios[$n]; }
        else {
            $dec = (int) $n / 10;
            $uni = (int) $n % 10;
            $result = $decimais[$dec - 2];
            if($uni != 0){
                $result += $unitarios[$uni];
            }
            $n = $result;
        }
    }

    echo "$n\n";
?>