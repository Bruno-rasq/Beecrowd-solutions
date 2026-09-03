<?php 

    list($a, $b, $c) = explode(" ", readline());

    $a = (int) $a;
    $b = (int) $b;
    $c = (int) $c;

    $vetor = [$a, $b, $c];

    for($i = 0; $i < count($vetor); $i++){
        for($j = 0; $j < count($vetor) - $i - 1; $j++){
            if($vetor[$j] > $vetor[$j + 1]){
                $temp = $vetor[$j + 1];
                $vetor[$j + 1] = $vetor[$j];
                $vetor[$j] = $temp;
            }
        }
    }

    foreach ($vetor as $valor){
        echo "$valor\n";
    }
    echo " \n";
    echo "$a\n";
    echo "$b\n";
    echo "$c\n";
?>