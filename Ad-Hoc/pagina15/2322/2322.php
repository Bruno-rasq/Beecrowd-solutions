<?php 

    $total_pecas = (int) readline();
    $pecas = explode(" ", readline());

    for($i = 1; $i <= $total_pecas; $i++){
        $encontrou = false;

        for($j = 0; $j < count($pecas); $j++){
            $curr = (int) $pecas[$j];

            if($curr == $i){
                $encontrou = true;
                break;
            }
        }

        if(!$encontrou){
            echo "$i\n";
            break;
        }
    }
?>