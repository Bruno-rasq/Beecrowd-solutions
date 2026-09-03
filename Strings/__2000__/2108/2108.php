<?php 

    $maior = 0;
    $maior_palavra = "";
    $line = readline();

    while($line != "0"){

        $resultado = "";
        $words = explode(' ', $line);

        for($i = 0; $i < count($words); $i++){
            if($resultado != ""){ $resultado .= "-"; }

            if (strlen($words[$i]) >= $maior){
                $maior = strlen($words[$i]);
                $maior_palavra = $words[$i];
            }

            $resultado .= strlen($words[$i]);
        }

        echo "$resultado\n";
        $line = readline();
    }
    echo "\n";
    echo "The biggest word: $maior_palavra\n";
?>