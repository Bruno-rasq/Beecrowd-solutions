<?php 

    while(($becteria_dna = readline()) !== false && ($code_genetico = readline()) !== false){

        $becteria_dna = trim($becteria_dna);
        $code_genetico = trim($code_genetico);

        if(strpos($becteria_dna, $code_genetico) !== false){
            echo "Resistente\n";
        } else {
            echo "Nao resistente\n";
        }
    }
?>