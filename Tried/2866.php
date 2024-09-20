<?php 

    $n = (int) readline();

    for ($i = 0; $i < $n; $i++) {
        $cryp = readline();
        $decryp = "";

        for ($j = 0; $j < strlen($cryp); $j++) {
            $currentChar = $cryp[$j];
            if (!ctype_upper($currentChar)) {
                $decryp .= $currentChar;
            }
        }

        $response = strrev($decryp);

        echo "$response\n";
    }

?>