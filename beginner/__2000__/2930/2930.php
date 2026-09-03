<?php 

    list($entraga, $prazo) = explode(" ", readline());

    $entraga = (int) $entraga; $prazo = (int) $prazo;

    if ($prazo - $entraga >= 1){

        echo "Muito bem!, Apresenta antes do Natal!\n";
    }
    
    elseif ($prazo - $entraga < 0){
    
        echo "Eu te odeio professora!\n";
    }
    
    elseif ($prazo - $entraga < 3){
    
        echo "Parece o trabalho do meu filho!\n";
        $prazo += 2;

        if ($prazo <= 24){
    
            echo "TCC Apresentado!\n";
        }
        else{
    
            echo "Fail! Entao eh nataaaaal!\n";
        }
    }
?>