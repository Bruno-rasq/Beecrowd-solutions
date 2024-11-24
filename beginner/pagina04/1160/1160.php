<?php 

    function crescimento_populacional($pa, $pb, $ga, $gb){
        $result = 1;
        for($i = 1; $i < 101; $i++){
            if($pa > $pb){ break; }

            $pa += intval($pa * $ga);
            $pb += intval($pb * $gb);

            $result += 1;
        }

        if($pa <= $pb){
            return "Mais de 1 seculo.";
        } else {
            return ($result - 1) + " anos.";
        }
    }

    $handle = fopen("php://stdin", "r");
    $n = intval(fgets($handle));

    for($i = 0; $i < $n; $i++){

        $line = fgets($handle);
        list($pa, $pb, $ga, $gb) = explode(" ", trim($line));

        $pa = intval($pa);
        $pb = intval($pb);
        $ga = floatval($ga) / 100;
        $gb = floatval($gb) / 100;
    

        $response = crescimento_populacional($pa, $pb, $ga, $gb);

        echo $response . PHP_EOL;
    }

    fclose($handle);
?>