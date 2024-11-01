<?php 

    while($ano = (int) readline()){

        if($ano <= 100){
            echo "1\n";
        } else {
            $seculo = (int) $ano / 100;
            if($ano % 100 != 0){
                $seculo += 1;
            }

            echo "$seculo\n";
        }
    }

?>