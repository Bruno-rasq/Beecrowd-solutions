<?php 

    function steps($n, $k){
        $result = 0;
        for($i = 2; $i < $n + 1; $i++){
            $result = ($result + $k) % $i;
        }
        return $result;
    }

    $n = (int) readline();
    for($i = 0; $i < $n; $i++){
        list($a,$b) = explode(" ", readline());
        $a = (int) $a;
        $b = (int) $b;
        $step = steps($a, $b) + 1;

        echo "Case " . ($i + 1) . ": $step\n";
    }
?>