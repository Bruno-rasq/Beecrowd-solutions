<?php 

    $n = intVal(trim(fgets(STDIN)));
    $t = 0;

    while($n != 0){

        if($t) echo "\n";

        $consumos = array_fill(0, 201, 0);
        $totalX = 0;
        $totalY = 0;

        for($i = 0; $i < $n; $i++){
            list($x, $y) = array_map('intval', explode(" ", readline()));

            $totalX += $x;
            $totalY += $y;

            $consumoPorPessoa = floor($y / $x);
            $consumos[$consumoPorPessoa] += $x;
        }

        echo "Cidade# " . (++$t) . ";\n";

        $output = [];
        for($i = 0; $i < 201; $i++){
            if($consumos[$i] > 0) $output[] = $consumos[$i] . "-" . $i;
        }

        echo implode(" ", $output) . "\n";

        $consumoTotal = floor(100 * ($totalY / $totalXl)) / 100;
        echo "Consumo medio " . number_format($consumoTotal, 2, '.', '') . " m3.\n";

        $n = intVal(trim(fgets(STDIN)));
        
    }

?>