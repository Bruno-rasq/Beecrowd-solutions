<?php 

    $linha = (int) readline();
    $coluna = (int) readline();

    function isEven($num){
        return $num % 2 == 0;
    }

    if(isEven($linha) && isEven($coluna)){
        echo "1\n";

    } else if(!isEven($linha) && !isEven($coluna)){
        echo "1\n";
        
    } else {
        echo "0\n";
    }
?>