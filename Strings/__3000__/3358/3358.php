<?php 

    $vogais = ['a', 'e', 'i', 'o', 'u'];
    $n = (int) readline();

    for($i = 0; $i < $n; $i++){

        $sobrenome = readline();
        $dificil = false;
        $contagem = 0;

        for($j = 0; $j < strlen($sobrenome); $j++){
            $letter = strtolower($sobrenome[$j]);

            if(!in_array($letter, $vogais)){
                $contagem++;
            } else {
                $contagem = 0;
            }

            if($contagem == 3){
                $dificil = true;
                break;
            }
        }

        if($dificil){
            echo "$sobrenome nao eh facil\n";
        } else {
            echo "$sobrenome eh facil\n";
        }
    }

?>