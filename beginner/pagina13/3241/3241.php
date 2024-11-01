<?php 

    $n = (int) readline();

    for($i = 0; $i < $n; $i++){
        $curr = readline();

        if($curr == "P=NP"){
            echo "skipped\n";
            continue;
        }

        list($a, $b) = explode("+", $curr);
        $a = (int) $a;
        $a = (int) $b;
        $resposta = $a + $b;

        echo "$resposta\n";
    }

?>