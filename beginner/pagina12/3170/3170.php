<?php 

    $b = (int) readline();
    $g = (int) readline();

    $result = intdiv($g, 2) - $b;

    if($result <= 0){
        
        echo"Amelia tem todas bolinhas!\n";
    } else {
        echo "Faltem $result bolinha(s)!\n";
    }
?>