<?php 

    // a corrigir
    while(true){
    
        $input = readline();

        if($input == false || $input == "") break;

        $jogadores = (int) $input;
        $doistercos = ceil($jogadores * (2/3));
        $votos = explode(" ", readline());
        $votosImpeachment = 0;

        for($i = 0; $i < $jogadores; $i++){
            if($votos[$i] == "1"){
                $votosImpeachment++;
            }
        }

        $response = $votosImpeachment >= $doisTercos 
        ? "impeachment" 
        : "acusacao arquivada";

        echo "$response\n";
    }
?>