<?php 

    while($line = fgets(STDIN)){

        list($ah, $am) = explode(' ', $line);
        $ah = (int) $ah;
        $am = (int) $am;


        $hora = floor($ah / 30);
        $minuto = floor($am / 6);

        $horaf = str_pad((string) $hora, 2, "0", STR_PAD_LEFT);
        $minutof = str_pad((string) $minuto, 2, "0", STR_PAD_LEFT);

        echo "$horaf:$minuotf\n";
    }

?>