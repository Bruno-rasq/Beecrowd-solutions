<?php 
    $input = explode("\n", trim(file_get_contents("php://stdin")));
    $index = 0;

    while (true){
        $n = (int) $input[$index++];
        if($n == 0) break;

        $posicao_atual = 2;
        $contador = 0;

        $posicoes = [
            '0 1 1' => 1,
            "1 0 1" => 2,
            "1 1 0" => 3
        ];

        for ($i = 0; $i < $n; $i++){
            $curr = $input[$index++];

            if(isset($posicoes[$curr]) && $posicoes[$curr] != $posicao_atual){
                $contador += abs($posicao_atual - $posicoes[$curr]);
                $posicao_atual = $posicoes[$curr];
            }
        }

        echo "$contador\n";
    }
?>