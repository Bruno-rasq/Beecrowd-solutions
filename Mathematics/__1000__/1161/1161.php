<?php 

    function fatorial ($n){
        if($n == 1 || $n == 0){
            return 1;
        }
        return $n * fatorial($n - 1);
    }

    while(($line = readline()) != false){

        if(trim($line) == '') break;

        list($a, $b) = explode(' ', $line);

        $a = (int) $a;
        $b = (int) $b;

        $fa = fatorial($a);
        $fb = fatorial($b);

        $soma = $fa + $fb;

        echo "$soma\n";
    }
?>