<?php 

    $Num = (float) readline();

    if($Num < 0 ){
        echo "Fora de intervalo\n";
    
    } else if ( $Num >= 0 && $Num <= 25 ){
        echo "Intervalo [0,25]\n";
    
    } else if ( $Num >= 25 && $Num <= 50 ){
        echo "Intervalo (25,50]\n";
    
    } else if( $Num >= 50 && $Num <= 75 ){
        echo "Intervalo (50,75]\n";
    
    } else if ( $Num >= 75 && $Num <= 100 ){
        echo "Intervalo (75,100]\n";
    
    } else if ( $Num > 100 ){
        echo "Fora de intervalo\n";
    }

?>