<?php 

    $n = (int) readline();
    $wins = 0;

    for($i = 0; $i < $n; $i++){
        $curr = readline();
        if(str_contains($curr, "CD")){
            continue;
        }
        $wins++;
    }

    echo "$wins\n";
?>