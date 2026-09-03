<?php 

    $output = "";

    while($input = readline()){
        list($lp, $ap, $qnt) = explode(" ", $input);

        $lp = (int) $lp; $ap = (int) $ap; $qnt = (int) $qnt;

        for($i = 0; $i < $qnt; $i++){
            list($lpc, $apc) = explode(' ', readline());
            
            $lpc = (int) $lpc; $apc = (int) $apc;

            if(($lpc <= $lp && $apc <= $ap) || ($lpc <= $ap && $apc <= $lp)){
                $output .= "Sim\n";
            } else {
                $output .= "Nao\n";
            }

        }
    }

    echo "$output";
?>